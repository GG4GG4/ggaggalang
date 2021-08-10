# ggaggalang
Built for fun, based on BrainFuck.

Syntax
------
pikalang  | brainfuck | description                                   
----------|-----------|-----------------------------------------------
`gga`      | +         | increment the byte at pointer                 
`kka`      | -         | decrement the byte at pointer                 
`ggagga`    | [         | if pointer is zero, jump to matching `gu`    
`gu`     | ]         | if pointer is nonzero, jump to matching `ggagga`
`gugu`    | >         | increment the data pointer                    
`gugugga`   | <         | decrement the data pointer                    
`guguggagga`  | ,         | input of one byte into pointer                
`gguggaggugga` | .         | output the byte at pointer    
