## Let's take a look at this in action

To the right you see two panes.

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
