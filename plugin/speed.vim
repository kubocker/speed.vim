" speed.vim
" Maintainer:  Takeshi Kubokawa <kubocker@gmail.com>
" Version:  0.0.1
"

"if (exists("g:loaded_todolist") && g:loaded_speed) || &cp
"    finish
"endif
"let g:loaded_speed = 1

if exists("g:loaded_speed")
    finish
endif

let s:save_cpo = &cpo
set cpo&vim

" ---- todo ---- "
if !exists('g:speed_todo_path')
    let g:speed_todo_path = $HOME . "/todo"
endif
" ---- memo ---- "
if !exists('g:speed_memo_path')
    let g:speed_memo_path = $HOME . "/memo"
endif
" ---- diary ---- "
if !exists('g:speed_diary_path')
    let g:speed_diary_path = $HOME . "/diary"
endif
"

command! -nargs=* Go : call Go(<f-args>)

let &cpo = s:save_cpo
unlet s:save_cpo

let g:loaded_speed = 1
