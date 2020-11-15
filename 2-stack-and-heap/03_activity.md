## Let's take a look at this in action

<iframe width="800px" height="400px" src="https://godbolt.org/e?hideEditorToolbars=true#g:!((g:!((g:!((h:codeEditor,i:(fontScale:14,j:1,lang:c%2B%2B,source:'//+Type+your+code+here,+or+load+an+example.%0Aint+square(int+num)+%7B%0A++++return+num+*+num%3B%0A%7D'),l:'5',n:'0',o:'C%2B%2B+source+%231',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:g102,filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'1',intel:'0',libraryCode:'1',trim:'1'),fontScale:14,j:1,lang:c%2B%2B,libs:!(),options:'',source:1),l:'5',n:'0',o:'x86-64+gcc+10.2+(Editor+%231,+Compiler+%231)+C%2B%2B',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0')),l:'2',n:'0',o:'',t:'0')),version:4"></iframe>

The above program  is written in _machine code_.

Given the function definitions below, try to figure out what the computer is doing on the right side

|   command    |               definition                    |
|--------------|---------------------------------------------|
| `push A`     | put the value A on the top of stack         |
| `mov A, B`   | copy the value in A to B                    |
| `DWORD PTR`  | convert to double word                      |
| `imul A, B`  | multiply the integer A by the integer B     |
| `pop A`      | pull the top off the stack and put it in A  |
| `ret`        | return                                      |
