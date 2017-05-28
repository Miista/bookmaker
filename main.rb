require 'json'
load 'IOUtils.rb'

class Keys
  DIRECTORY = "dir"
  TITLE = "title"
  DATA_FILE = "datafile"
  ADDITIONAL_DIRS = "add_dirs"
end

def mk_dir_name(str)
  return str.gsub(' ', '-').downcase
end

def create_book(root)
  chapterDir = File.join(root, "chapters")
  characterDir = File.join(root, "characters")

  Dir.mkdir(root)
  Dir.mkdir(chapterDir)
  Dir.mkdir(characterDir)
end

def write_config(config)
  root = config[Keys::DIRECTORY]
  config_file = File.join(root, ".books")
  File.open(config_file, "w") do |f|
    f.write(config.to_json)
  end
end

title = get_input("Title")
confirmation = confirm("Create new book with title \"#{title}\"?")
if confirmation then
  bookData = {
    Keys::TITLE => title,
    Keys::DIRECTORY => mk_dir_name(title),
    Keys::ADDITIONAL_DIRS => []
  }
  root = bookData[Keys::DIRECTORY]
  create_book(root)
  write_config(bookData)
  puts "Book created!"
end
