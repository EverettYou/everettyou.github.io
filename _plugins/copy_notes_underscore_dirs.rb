# frozen_string_literal: true
require "fileutils"
# Copy Jupyter Book output dirs (_static, _sources, _sphinx_design_static) into
# _site because Jekyll does not copy directories whose names start with _.
Jekyll::Hooks.register :site, :post_write do |site|
  notes_src = File.join(site.source, "teaching", "PHYS2C", "notes")
  notes_dest = File.join(site.dest, "teaching", "PHYS2C", "notes")
  %w[_static _sources _sphinx_design_static].each do |dir|
    src = File.join(notes_src, dir)
    dest = File.join(notes_dest, dir)
    next unless File.directory?(src)
    FileUtils.mkdir_p(File.dirname(dest))
    FileUtils.rm_r(dest, :secure => true) if File.exist?(dest)
    FileUtils.cp_r(src, dest)
  end
end
