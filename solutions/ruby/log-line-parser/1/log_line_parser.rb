class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    #splitting message
    msg_start = @line.index(" ") + 1
    msg_strip = @line.slice(msg_start, @line.size)
    #cleaning the message with regex
    return msg_strip.gsub(/[\t\r\n]/, "").strip
  end

  def log_level
    log_end = @line.index(":") - 2
    return @line.slice(1, log_end).downcase
  end

  def reformat
    return "#{self.message} (#{self.log_level})"
  end
end
