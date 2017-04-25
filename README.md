# speed.vim


#### to support your developing or work

## Set Up

#####  set vim8 and python3
-  mac
```bash
$ brew install vim --with-python3
$ brew install python3
```

##### set plugin at ~/.vimrc
- vim-plug
```vim
Plug 'kubocker/speed.vim', {'do': 'pip install TinyDB'}
:PlugInstall
```
- NeoBundle
```vim
NeoBundle 'kubocker/speed.vim'
:NeoBundleInstall
```
```bash
$ pip install TinyDB
```

- dein.vim
```vim
call dein#add('kubocker/speed.vim')
vim
```
```bash
$ pip install TinyDB
```

- path
```vim
let g:speed_todo_path = <your path>
```

## commands

#### todo

> list
- Samples
```vim
:Go todo list
:Go todo list today
:Go todo list yesterday
:Go todo list tmorrow
```

> add
- Samples
```vim
:Go todo add 2017 4 28 "機械学習_勉強会_参加"
:Go todo add 2017 4 29 "お食事デート"
```

> all
- Samples
```vim
:Go todo all
```



### memo

### diary


## next update list

