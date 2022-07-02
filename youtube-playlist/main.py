import shlex

database = {}

def new(playlist):
  if playlist in database:
    print(f'Playlist {playlist} already exists')
    return
  database[playlist] = []
  print(f'Created playlist {playlist}')

def list_command():
  print('Playlists:')
  for playlist in database:
    print(playlist)

def remove_list(playlist):
  if playlist not in database:
    print(f'Playlist {playlist} does not exist')
    return
  del database[playlist]
  print(f'Removed playlist {playlist}')

def remove_item(playlist, index):
  if playlist not in database:
    print(f'Playlist {playlist} does not exist')
    return
  if index < 0 or index >= len(database[playlist]):
    print(f'Index {index} out of range')
    return
  del database[playlist][index]

def insert(playlist, link):
  if playlist not in database:
    print(f'Playlist {playlist} does not exist')
    return
  if link in database[playlist]:
    print(f'Link {link} already exists')
    return
  database[playlist].append(link)
  print(f'Added {link} to {playlist}')

def show(playlist):
  if playlist not in database:
    print(f'Playlist {playlist} does not exist')
    return
  print(f'Playlist {playlist}')
  for i, link in enumerate(database[playlist]):
    print(f'{i}: {link}')

def main():
  print('YouTube Playlist CLI')
  while True:
    args = shlex.split(input('> '))
    if len(args) == 0:
      continue
    command = args[0]
    match command:
      case 'new':
        if len(args) < 2:
          print('Usage: new <playlist>')
          continue
        new(args[1])
      case 'list':
        list_command()
      case 'removelist':
        if len(args) < 2:
          print('Usage: removelist <playlist>')
          continue
        remove_list(args[1])
      case 'removeitem':
        if len(args) < 3:
          print('Usage: removeitem <playlist> <index>')
          continue
        remove_item(args[1], args[2])
      case 'insert':
        if len(args) < 3:
          print('Usage: insert <playlist> <link>')
          continue
        insert(args[1], args[2])
      case 'show':
        if len(args) < 2:
          print('Usage: show <playlist>')
          continue
        show(args[1])
      case 'exit':
        break

if __name__ == '__main__':
  main()