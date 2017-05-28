require 'json'
load 'IOUtils.rb'

# File.open(".book", "r") do |f|
#   s = f.read
#   puts JSON.parse(s)
# end
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

def mk_dir_name(str)
  return str.gsub(' ', '-').downcase
end

title = get_input("Title")
confirmation = confirm("Create new book with title \"#{title}\"?")
if confirmation then
  bookData = {
    "title" => title,
    "dir" => mk_dir_name(title)
  }
  root = bookData["dir"]
  Dir.mkdir(root)
  Dir.mkdir(File.join(root, "chapters"))
  Dir.mkdir(File.join(root, "characters"))
  File.open(File.join(root, ".books"), "w") do |f|
    f.write(bookData.to_json)
  end
  puts Dir.getwd
end
