# frozen_string_literal: true
require "fileutils"
# Copy Jupyter Book output dirs (_static, _sources, _sphinx_design_static) into _site
# under names WITHOUT leading underscore (static, sources, sphinx_design_static) so
# GitHub Pages will serve them (it does not serve _* paths). Then rewrite HTML refs.
Jekyll::Hooks.register :site, :post_write do |site|
  notes_src = File.join(site.source, "teaching", "PHYS2C", "notes")
  notes_dest = File.join(site.dest, "teaching", "PHYS2C", "notes")
  # Map underscore dir -> deploy name (no underscore)
  dir_map = {
    "_static" => "static",
    "_sources" => "sources",
    "_sphinx_design_static" => "sphinx_design_static"
  }
  dir_map.each do |underscore_dir, deploy_name|
    src = File.join(notes_src, underscore_dir)
    dest = File.join(notes_dest, deploy_name)
    next unless File.directory?(src)
    FileUtils.mkdir_p(File.dirname(dest))
    FileUtils.rm_r(dest, :secure => true) if File.exist?(dest)
    FileUtils.cp_r(src, dest)
  end

  # Rewrite HTML in notes so asset paths use deploy names (static, sources, ...)
  html_dir = notes_dest
  if File.directory?(html_dir)
    Dir.glob(File.join(html_dir, "*.html")).each do |path|
      content = File.read(path, :encoding => "utf-8")
      new_content = content
        .gsub(/_static\b/, "static")
        .gsub(/_sources\b/, "sources")
        .gsub(/_sphinx_design_static\b/, "sphinx_design_static")
      # Remove duplicate THEBE_JS_URL / togglebuttonSelector script block (Jupyter Book bug)
      dup = "    <script>var togglebuttonSelector = '.toggle, .admonition.dropdown';</script>\n    <script>const THEBE_JS_URL = \"https://unpkg.com/thebe@0.8.2/lib/index.js\"; const thebe_selector = \".thebe,.cell\"; const thebe_selector_input = \"pre\"; const thebe_selector_output = \".output, .cell_output\"</script>"
      new_content = new_content.sub(dup, "")
      File.write(path, new_content, :encoding => "utf-8") if new_content != content
    end
  end
end
