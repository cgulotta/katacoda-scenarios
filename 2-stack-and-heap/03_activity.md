## Let's take a look at this in action

Below you see two panes.

<iframe width="800px" height="200px" src="https://godbolt.org/e?readOnly=true&hideEditorToolbars=true#g:!((g:!((g:!((h:codeEditor,i:(fontScale:14,j:1,lang:python,selection:(endColumn:16,endLineNumber:2,positionColumn:16,positionLineNumber:2,selectionStartColumn:16,selectionStartLineNumber:2,startColumn:16,startLineNumber:2),source:'def+square(a):%0A++++return+a*a%3B'),l:'5',n:'0',o:'Python+source+%231',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:python36,filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'1',intel:'0',libraryCode:'1',trim:'1'),fontScale:14,j:1,lang:python,libs:!(),options:'',selection:(endColumn:1,endLineNumber:1,positionColumn:1,positionLineNumber:1,selectionStartColumn:1,selectionStartLineNumber:1,startColumn:1,startLineNumber:1),source:1),l:'5',n:'0',o:'Python+3.6+(Editor+%231,+Compiler+%231)+Python',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0')),l:'2',n:'0',o:'',t:'0')),version:4"></iframe>

The left one is a function (written in C++) which returns the square of a provided number.

The right one, is the same program converted to _machine code_.

Both programs are executed from top to bottom.

Given the function definitions below, try to figure out what the computer is doing on the right side

|   command    |               definition                    |
|--------------|---------------------------------------------|
| `push A`     | put the value A on the top of stack         |
| `mov A, B`   | copy the value in A to B                    |
| `DWORD PTR`  | convert to double word                      |
| `imul A, B`  | multiply the integer A by the integer B     |
| `pop A`      | pull the top off the stack and put it in A  |
| `ret`        | return                                      |
