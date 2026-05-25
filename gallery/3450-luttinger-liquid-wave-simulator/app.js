const state = {
  data: null,
  currentFrame: 0,
  isPlaying: false,
  playbackTimer: null,
  playbackSpeed: 1,
  autoRunTimer: null,
  requestSerial: 0,
};

const TAU = 2 * Math.PI;
const PLAYBACK_BASE_MS = 90;
const AUTO_RUN_DELAY_MS = 450;
const CHANNEL_COLORS = ["#c93300", "#ff8f29", "#009926", "#0073e6"];
const K_INV_DIAG = [1, 1, -1, -1];
const ELL_1 = [1, -2, 1, 2];
const ELL_2 = [-3, 1, 1, -3];

const form = document.getElementById("control-form");
const statusText = document.getElementById("status-text");
const playToggle = document.getElementById("play-toggle");
const restartButton = document.getElementById("restart-button");
const speedSelect = document.getElementById("speed-select");
const timeSlider = document.getElementById("time-slider");
const timeLabel = document.getElementById("time-label");
const xMinLabel = document.getElementById("x-min-label");
const xMidLabel = document.getElementById("x-mid-label");
const xMaxLabel = document.getElementById("x-max-label");
const channelPlots = Array.from({ length: 4 }, (_, index) =>
  document.getElementById(`channel-plot-${index}`),
);

function setStatus(message, isError = false) {
  statusText.textContent = message;
  statusText.style.color = isError ? "#ffb0a0" : "";
}

function setPlayIcon(isPlaying) {
  playToggle.innerHTML = `<i class="fa-solid ${isPlaying ? "fa-pause" : "fa-play"}" aria-hidden="true"></i>`;
  playToggle.setAttribute("aria-label", isPlaying ? "Pause simulation" : "Play simulation");
}

function wrapCompactField(value) {
  return ((value + Math.PI) % TAU + TAU) % TAU - Math.PI;
}

function collectPayload() {
  const data = new FormData(form);
  return {
    g0: Number(data.get("g0")),
    interface_width: Number(data.get("interface_width")),
    interface_center: Number(data.get("interface_center")),
    interaction_side: data.get("interaction_side"),
    packet_channel: Number(data.get("packet_channel")),
    packet_amplitude: Number(data.get("packet_amplitude")),
    packet_center: Number(data.get("packet_center")),
    packet_width: Number(data.get("packet_width")),
    x_min: Number(data.get("x_min")),
    x_max: Number(data.get("x_max")),
    num_points: Number(data.get("num_points")),
    dt: Number(data.get("dt")),
    num_steps: Number(data.get("num_steps")),
    sample_every: Number(data.get("sample_every")),
    boundary: data.get("boundary"),
    v_diag: [
      Number(data.get("v1")),
      Number(data.get("v2")),
      Number(data.get("v3")),
      Number(data.get("v4")),
    ],
  };
}

function scale(value, min, max, outputMin, outputMax) {
  if (max === min) return (outputMin + outputMax) / 2;
  return outputMin + ((value - min) / (max - min)) * (outputMax - outputMin);
}

function createWavePath(values, xValues, width, height) {
  const paddingX = 18;
  const paddingY = 20;
  const commands = values.map((value, index) => {
    const x = scale(xValues[index], xValues[0], xValues[xValues.length - 1], paddingX, width - paddingX);
    const y = scale(wrapCompactField(value), -Math.PI, Math.PI, height - paddingY, paddingY);
    return `${index === 0 ? "M" : "L"} ${x.toFixed(2)} ${y.toFixed(2)}`;
  });
  return commands.join(" ");
}

function createCouplingBackground(width, height, channelIndex) {
  if (!state.data?.g_profile) return "";

  const gValues = state.data.g_profile;
  const stopCount = Math.min(80, gValues.length);
  const stops = [];

  for (let stopIndex = 0; stopIndex < stopCount; stopIndex += 1) {
    const sourceIndex = Math.round((stopIndex / Math.max(1, stopCount - 1)) * (gValues.length - 1));
    const strength = Math.max(0, Math.min(1, gValues[sourceIndex]));
    const opacity = (0.24 * strength).toFixed(3);
    stops.push(
      `<stop offset="${((stopIndex / Math.max(1, stopCount - 1)) * 100).toFixed(2)}%" stop-color="var(--sim-muted)" stop-opacity="${opacity}"></stop>`,
    );
  }

  return `
    <defs>
      <linearGradient id="coupling-gradient-${channelIndex}" x1="0" x2="1" y1="0" y2="0">
        ${stops.join("")}
      </linearGradient>
    </defs>
    <rect x="18" y="0" width="${width - 36}" height="${height}" fill="url(#coupling-gradient-${channelIndex})"></rect>
  `;
}

function createPlotGrid(width, height) {
  const paddingX = 18;
  const vertical = Array.from({ length: 7 }, (_, index) => {
    const x = paddingX + (index / 6) * (width - 2 * paddingX);
    return `<line x1="${x.toFixed(2)}" y1="0" x2="${x.toFixed(2)}" y2="${height}" class="screen-grid-line vertical"></line>`;
  }).join("");
  const horizontal = [20, height / 2, height - 20]
    .map((y, index) => {
      const className = index === 1 ? "screen-grid-line strong" : "screen-grid-line";
      return `<line x1="${paddingX}" y1="${y}" x2="${width - paddingX}" y2="${y}" class="${className}"></line>`;
    })
    .join("");
  return `${vertical}${horizontal}`;
}

function interfaceMarkerX(width) {
  if (!state.data?.meta) return null;
  const center = state.data.meta.interface_center;
  if (typeof center !== "number") return null;
  const xValues = state.data.x;
  if (center < xValues[0] || center > xValues[xValues.length - 1]) return null;
  return scale(center, xValues[0], xValues[xValues.length - 1], 18, width - 18);
}

function renderChannel(channelIndex) {
  if (!state.data) return;

  const width = 900;
  const height = 180;
  const svg = channelPlots[channelIndex];
  const frame = state.data.fields[state.currentFrame][channelIndex];
  const path = createWavePath(frame, state.data.x, width, height);
  const color = CHANNEL_COLORS[channelIndex];
  const marker = interfaceMarkerX(width);
  const markerMarkup =
    marker === null
      ? ""
      : `<line x1="${marker.toFixed(2)}" y1="18" x2="${marker.toFixed(2)}" y2="${height - 18}" class="interface-marker"></line>`;

  svg.innerHTML = `
    <rect x="0" y="0" width="${width}" height="${height}" class="screen-bg"></rect>
    ${createCouplingBackground(width, height, channelIndex)}
    ${createPlotGrid(width, height)}
    ${markerMarkup}
    <path d="${path}" fill="none" stroke="${color}" stroke-width="3" vector-effect="non-scaling-stroke" stroke-linecap="round" stroke-linejoin="round"></path>
  `;
}

function formatTick(value) {
  if (!Number.isFinite(value)) return "";
  if (Math.abs(value) < 1e-9) return "0";
  if (Math.abs(value) >= 10) return value.toFixed(0);
  return value.toFixed(2).replace(/0+$/, "").replace(/\.$/, "");
}

function updateSharedXAxis() {
  if (!state.data?.x?.length) return;
  const xValues = state.data.x;
  const xMin = xValues[0];
  const xMax = xValues[xValues.length - 1];
  const xMid = 0.5 * (xMin + xMax);

  xMinLabel.textContent = formatTick(xMin);
  xMidLabel.textContent = formatTick(xMid);
  xMaxLabel.textContent = formatTick(xMax);
}

function updateFrameDisplay() {
  if (!state.data) return;

  state.currentFrame = Math.min(state.currentFrame, state.data.times.length - 1);
  timeSlider.max = String(state.data.times.length - 1);
  timeSlider.value = String(state.currentFrame);
  timeLabel.textContent = state.data.times[state.currentFrame].toFixed(3);
  updateSharedXAxis();
  channelPlots.forEach((_, index) => renderChannel(index));
}

function validatePayload(payload) {
  if (payload.x_max <= payload.x_min) {
    throw new Error("x max must be larger than x min.");
  }
  if (payload.num_points < 64 || payload.num_points > 800) {
    throw new Error("Grid points must be between 64 and 800.");
  }
  if (payload.dt <= 0 || payload.dt > 0.2) {
    throw new Error("dt must be in the interval (0, 0.2].");
  }
  if (payload.num_steps < 1 || payload.num_steps > 5000) {
    throw new Error("Steps must be between 1 and 5000.");
  }
  if (payload.sample_every < 1 || payload.sample_every > 200) {
    throw new Error("Sample every must be between 1 and 200.");
  }
  if (payload.g0 < 0 || payload.g0 > 10) {
    throw new Error("g0 must be between 0 and 10.");
  }
  if (payload.interface_width <= 0.05 || payload.interface_width > 20) {
    throw new Error("w must be in the interval (0.05, 20].");
  }
  if (payload.packet_amplitude <= 0 || payload.packet_amplitude > 5) {
    throw new Error("Amplitude must be in the interval (0, 5].");
  }
  if (payload.packet_width <= 0.05 || payload.packet_width > 10) {
    throw new Error("Packet width must be in the interval (0.05, 10].");
  }
  if (payload.v_diag.some((value) => value <= 0)) {
    throw new Error("All diagonal velocities must be positive.");
  }
}

function linspace(xMin, xMax, count, endpoint = true) {
  const values = new Array(count);
  const denominator = endpoint ? count - 1 : count;
  const dx = (xMax - xMin) / denominator;
  for (let index = 0; index < count; index += 1) {
    values[index] = xMin + index * dx;
  }
  return { values, dx };
}

function sigmoidProfile(xValues, payload) {
  return xValues.map((x) => {
    const argument = payload.interaction_side === "right"
      ? -(x - payload.interface_center) / payload.interface_width
      : (x - payload.interface_center) / payload.interface_width;
    return payload.g0 / (1 + Math.exp(argument));
  });
}

function createInitialField(xValues, payload) {
  const fields = Array.from({ length: 4 }, () => new Array(xValues.length).fill(0));
  const channel = payload.packet_channel;
  for (let index = 0; index < xValues.length; index += 1) {
    const z = (xValues[index] - payload.packet_center) / payload.packet_width;
    fields[channel][index] = payload.packet_amplitude * Math.exp(-0.5 * z * z);
  }
  return fields;
}

function cloneField(phi) {
  return phi.map((channel) => channel.slice());
}

function addScaledField(phi, velocity, scaleFactor) {
  return phi.map((channel, channelIndex) =>
    channel.map((value, pointIndex) => value + scaleFactor * velocity[channelIndex][pointIndex]),
  );
}

function combineRk4(phi, k1, k2, k3, k4, dt) {
  return phi.map((channel, channelIndex) =>
    channel.map((value, pointIndex) =>
      value
      + (dt / 6)
        * (
          k1[channelIndex][pointIndex]
          + 2 * k2[channelIndex][pointIndex]
          + 2 * k3[channelIndex][pointIndex]
          + k4[channelIndex][pointIndex]
        ),
    ),
  );
}

function firstDerivative(phi, dx, boundary) {
  const pointCount = phi[0].length;
  return phi.map((channel) => {
    const derivative = new Array(pointCount);
    if (boundary === "periodic") {
      for (let index = 0; index < pointCount; index += 1) {
        const left = index === 0 ? pointCount - 1 : index - 1;
        const right = index === pointCount - 1 ? 0 : index + 1;
        derivative[index] = (channel[right] - channel[left]) / (2 * dx);
      }
      return derivative;
    }

    derivative[0] = (channel[1] - channel[0]) / dx;
    derivative[pointCount - 1] = (channel[pointCount - 1] - channel[pointCount - 2]) / dx;
    for (let index = 1; index < pointCount - 1; index += 1) {
      derivative[index] = (channel[index + 1] - channel[index - 1]) / (2 * dx);
    }
    return derivative;
  });
}

function nonlinearForce(phi, gProfile) {
  const pointCount = phi[0].length;
  const force = Array.from({ length: 4 }, () => new Array(pointCount).fill(0));
  for (let pointIndex = 0; pointIndex < pointCount; pointIndex += 1) {
    let phase1 = 0;
    let phase2 = 0;
    for (let channelIndex = 0; channelIndex < 4; channelIndex += 1) {
      phase1 += ELL_1[channelIndex] * phi[channelIndex][pointIndex];
      phase2 += ELL_2[channelIndex] * phi[channelIndex][pointIndex];
    }
    const sin1 = Math.sin(phase1);
    const sin2 = Math.sin(phase2);
    const coupling = 2 * Math.PI * gProfile[pointIndex];
    for (let channelIndex = 0; channelIndex < 4; channelIndex += 1) {
      force[channelIndex][pointIndex] =
        coupling * (ELL_1[channelIndex] * sin1 + ELL_2[channelIndex] * sin2);
    }
  }
  return force;
}

function integrateAlongX(source, dx) {
  return source.map((channel) => {
    const integral = new Array(channel.length).fill(0);
    for (let index = 1; index < channel.length; index += 1) {
      integral[index] = integral[index - 1] + 0.5 * (channel[index] + channel[index - 1]) * dx;
    }
    const mean = integral.reduce((sum, value) => sum + value, 0) / integral.length;
    return integral.map((value) => value - mean);
  });
}

function rhs(phi, grid, payload, gProfile) {
  const phiX = firstDerivative(phi, grid.dx, payload.boundary);
  const force = nonlinearForce(phi, gProfile);
  const source = force.map((channel, channelIndex) =>
    channel.map((value) => K_INV_DIAG[channelIndex] * value),
  );
  const interactionVelocity = integrateAlongX(source, grid.dx);

  return phi.map((channel, channelIndex) =>
    channel.map((_, pointIndex) =>
      K_INV_DIAG[channelIndex] * payload.v_diag[channelIndex] * phiX[channelIndex][pointIndex]
      - interactionVelocity[channelIndex][pointIndex],
    ),
  );
}

function rk4Step(phi, grid, payload, gProfile) {
  const k1 = rhs(phi, grid, payload, gProfile);
  const k2 = rhs(addScaledField(phi, k1, 0.5 * payload.dt), grid, payload, gProfile);
  const k3 = rhs(addScaledField(phi, k2, 0.5 * payload.dt), grid, payload, gProfile);
  const k4 = rhs(addScaledField(phi, k3, payload.dt), grid, payload, gProfile);
  return combineRk4(phi, k1, k2, k3, k4, payload.dt);
}

function simulateInBrowser(payload) {
  validatePayload(payload);
  const endpoint = payload.boundary !== "periodic";
  const grid = linspace(payload.x_min, payload.x_max, payload.num_points, endpoint);
  const gProfile = sigmoidProfile(grid.values, payload);
  let phi = createInitialField(grid.values, payload);
  const fields = [cloneField(phi)];
  const times = [0];

  for (let step = 1; step <= payload.num_steps; step += 1) {
    phi = rk4Step(phi, grid, payload, gProfile);
    if (step % payload.sample_every === 0) {
      fields.push(cloneField(phi));
      times.push(step * payload.dt);
    }
  }

  return {
    x: grid.values,
    times,
    fields,
    g_profile: gProfile,
    meta: {
      dt: payload.dt,
      num_steps: payload.num_steps,
      sample_every: payload.sample_every,
      boundary: payload.boundary,
      interface_center: payload.interface_center,
      interaction_side: payload.interaction_side,
      runtime: "browser",
    },
  };
}

function stopPlayback() {
  state.isPlaying = false;
  setPlayIcon(false);
  if (state.playbackTimer !== null) {
    clearInterval(state.playbackTimer);
    state.playbackTimer = null;
  }
}

function advanceFrame() {
  if (!state.data) return;
  state.currentFrame += 1;
  if (state.currentFrame >= state.data.times.length) {
    state.currentFrame = 0;
  }
  updateFrameDisplay();
}

function startPlayback() {
  if (!state.data || state.data.times.length <= 1) return;
  stopPlayback();
  state.isPlaying = true;
  setPlayIcon(true);
  state.playbackTimer = window.setInterval(advanceFrame, PLAYBACK_BASE_MS / state.playbackSpeed);
}

async function runSimulation({ keepStatus = false } = {}) {
  stopPlayback();
  const requestId = ++state.requestSerial;
  if (!keepStatus) {
    setStatus("Running browser-side nonlinear PDE simulation...");
  }

  try {
    await new Promise((resolve) => window.setTimeout(resolve, 0));
    const payload = simulateInBrowser(collectPayload());
    if (requestId !== state.requestSerial) return;

    state.data = payload;
    state.currentFrame = 0;
    updateFrameDisplay();
    if (window.MathJax?.typesetPromise) {
      window.MathJax.typesetPromise();
    }
    setStatus(`Simulation complete: ${payload.times.length} frames stored.`);
  } catch (error) {
    if (requestId === state.requestSerial) {
      setStatus(error.message || "Simulation failed.", true);
    }
  } finally {
  }
}

function scheduleAutoRun() {
  if (state.autoRunTimer !== null) {
    clearTimeout(state.autoRunTimer);
  }
  setStatus("Parameter changed; auto-running...");
  state.autoRunTimer = window.setTimeout(() => {
    state.autoRunTimer = null;
    runSimulation({ keepStatus: true });
  }, AUTO_RUN_DELAY_MS);
}

function reflectCentersAboutOrigin() {
  for (const name of ["packet_center", "interface_center"]) {
    const input = form.elements.namedItem(name);
    if (!(input instanceof HTMLInputElement)) continue;

    const value = Number(input.value);
    if (Number.isFinite(value)) {
      input.value = String(-value);
    }
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
});

form.addEventListener("input", (event) => {
  if (event.target instanceof HTMLInputElement && event.target.type === "submit") return;
  scheduleAutoRun();
});

form.addEventListener("change", (event) => {
  if (event.target instanceof HTMLInputElement && event.target.name === "interaction_side") {
    reflectCentersAboutOrigin();
  }
  scheduleAutoRun();
});

timeSlider.addEventListener("input", () => {
  stopPlayback();
  state.currentFrame = Number(timeSlider.value);
  updateFrameDisplay();
});

speedSelect.addEventListener("change", () => {
  state.playbackSpeed = Number(speedSelect.value);
  if (state.isPlaying) {
    startPlayback();
  }
});

playToggle.addEventListener("click", () => {
  if (state.isPlaying) {
    stopPlayback();
  } else {
    startPlayback();
  }
});

restartButton.addEventListener("click", () => {
  stopPlayback();
  state.currentFrame = 0;
  updateFrameDisplay();
});

window.addEventListener("load", () => {
  setPlayIcon(false);
  runSimulation();
});
