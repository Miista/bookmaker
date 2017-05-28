def get_input(text)
  print "#{text}: "
  return gets.chomp
end

def confirm(text, enter_confirms = false)
  print "#{text} [y/n]: "
  resp = gets.chomp.downcase
  if resp == 'y' then
    return true
  elsif resp.empty? && enter_confirms then
    return true
  else
    return false
  end
end
