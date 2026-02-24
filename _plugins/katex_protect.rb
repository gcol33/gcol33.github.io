# Protect LaTeX math from kramdown processing
# Strategy: Replace math blocks with unique placeholders before kramdown, restore after

module Jekyll
  class KatexProtect
    @@display_blocks = {}
    @@inline_blocks = {}
    @@counter = 0

    def self.reset
      @@display_blocks = {}
      @@inline_blocks = {}
      @@counter = 0
    end

    def self.protect(content)
      reset

      # Protect display math $$...$$ (multiline)
      content = content.gsub(/\$\$([\s\S]+?)\$\$/) do
        key = "KATEXDISPLAY#{@@counter}XETAKEND"
        @@display_blocks[key] = $1
        @@counter += 1
        key
      end

      # Protect inline math $...$ (not $$, and content doesn't contain newlines)
      content = content.gsub(/(?<!\$)\$(?!\$)([^\$\n]+?)\$(?!\$)/) do
        key = "KATEXINLINE#{@@counter}XETAKEND"
        @@inline_blocks[key] = $1
        @@counter += 1
        key
      end

      [content, @@display_blocks.dup, @@inline_blocks.dup]
    end

    def self.restore(content, display_blocks, inline_blocks)
      # Restore display math
      display_blocks.each do |key, block|
        content = content.gsub(key, "$$#{block}$$")
      end

      # Restore inline math
      inline_blocks.each do |key, block|
        content = content.gsub(key, "$#{block}$")
      end

      content
    end
  end
end

# Store math blocks before rendering
Jekyll::Hooks.register [:documents, :pages], :pre_render do |doc|
  next unless doc.content
  doc.content, doc.data['_display_math'], doc.data['_inline_math'] = Jekyll::KatexProtect.protect(doc.content)
end

# Restore math blocks after rendering
Jekyll::Hooks.register [:documents, :pages], :post_render do |doc|
  next unless doc.output
  display = doc.data['_display_math'] || {}
  inline = doc.data['_inline_math'] || {}
  next if display.empty? && inline.empty?
  doc.output = Jekyll::KatexProtect.restore(doc.output, display, inline)
end
