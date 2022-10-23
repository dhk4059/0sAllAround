testcode = [
    '''func main

 assign v1 20
 funccall print v1

endfunc''',
#     '''func main
#   funccall input "Enter a name: "
#   funccall print "Hello, " result 
# endfunc''',
'''func main
  # comment 1
  assign i 0
  # comment 2
  # comment 3
  funccall print "output: " i  # outputs 0
endfunc''',
'''func main
  assign s 1234
  funccall strtoint "1234"
  assign n result
  funccall print "output: " n " has been converted"
  funccall x
  assign result -5
  funccall print "result: " result
  funccall print "this is a string"
  funccall print "this is also a string #### : helloworld"
  funccall x
endfunc

func x
  funccall print "hello"
  return + 5 95
  # this code is never reached
  funccall print "world"
endfunc''',
'''func main
  assign var1 6
  assign var2 1
  assign test1 & True & > var1 5 <= var2 4
  assign str1 "hello"
  assign str2 "world"
  assign test2 | != str1 str2 False
  funccall print "test1: " test1
  funccall print "test2: " test2
endfunc''',
'''func main
  funccall factorial
  assign bar result  # bar gets a value of 7
  funccall returns_nuthin
  funccall print result  # result still has a value of 7
endfunc

func factorial
  return 7
endfunc

func returns_nuthin   
endfunc''',
'''func main
  assign b 3
  assign a + 1 b
  funccall print a
  assign a * 2 b
  funccall print a
  assign a - 2 b
  funccall print a
  assign a / 20 b
  funccall print a
  assign a % 20 b
  funccall print a
  assign a > b 0
  funccall print a
  assign a > 0 b
  funccall print a
  assign a >= b 0
  funccall print a
  assign a >= 0 b
  funccall print a
  assign a >= b b
  funccall print a
  assign a <= b b
  funccall print a
  assign a & True True
  funccall print a
  assign a & False True
  funccall print a
  assign a | True True
  funccall print a
  assign a | False True
  funccall print a
  assign a | False False
  funccall print a
endfunc''',
'''func main
  assign i 0
  while < i 2 
    funccall print "Outer: " i
    assign j 3 
    while > j 0
      funccall print "Inner: " j
      assign j - j 1
    endwhile
    funccall print "Outer end: " i
    assign i + i 1
  endwhile
  assign x 0
  while > x 10
    assign x + x 1
  endwhile
  funccall print "x is now: " x
endfunc''',
'''func main
  assign n 5
  assign f 1
  funccall fact
  funccall print result
endfunc

func fact
  if == n 0
    return f
  endif
  assign f * f n
  assign n - n 1
  funccall fact
  return result
endfunc''',
'''#mutually recursive functions

func even
    if == n 0
        return True
    endif
    assign n - n 1
    funccall odd
    return result
endfunc

func odd
    if == n 0
        return False
    endif
    assign n - n 1
    funccall even
    return result
endfunc

func isEven
    funccall even
    if == result True
        funccall print "number is even"
    else
        funccall print "number is odd"
    endif
endfunc

func main
    assign n 15
    funccall isEven
    assign n 20
    funccall isEven
    assign n 0
    funccall isEven
    assign n 148
    funccall isEven
    assign n 548
    funccall isEven
endfunc''',
'''#double a string, recursively

func main
    assign n 4
    assign result "a"
    funccall double
    funccall print result

    assign n 6
    assign result "##"
    funccall double
    funccall print result

endfunc

func double
    if == n 0
        return
    endif
    assign n - n 1
    assign result + result result
    funccall double
endfunc''',
'''func Meta_return_offers
  funccall print "Does not exist"
endfunc

func main # OH BOY OUR MAIN
  assign i1 1
  assign i2 1
  assign iter 0
  funccall print i1
  funccall print i2
  assign flag False
  funccall fibonacci # <-- Call fibonacci

  assign bool True
  ###
  # next line tests if you can concatenate different types!
  ###

  funccall print result result "test" True bool "'True'"
  funccall strtoint result
  assign x + 0 result # Checking to see if you can add, since we converted it to an int!
  # You should not get a type error from this line!

  funccall print result

  # <(^_^<)
  ###
  # next set of lines examine if statements and changing conditions
  ###

  if == iter 10
    if == iter 11
      funccall print "should not run"
    endif

    assign iter + 10 10

    if == iter 20
      funccall print "should run!"
    endif

    while != iter 0
      assign x / result iter
      if == 0 % x 2 # So this prints if we have an even int!
        # WOW A RANDOM COMMENT
        funccall print x ", even!"
      else
        funccall print x ", odd!"#"Your parser better remove this"
      endif
      assign iter - iter 1

      # Just for the sake of further testing
      # Let's see if our Brew-In can handle func calls nested
      # inside ifs and whiles!

      assign flag True  # Let's take advantage of our global variables!
      funccall fibonacci

    endwhile

  else
    funccall print "should not run!"
  endif

endfunc

func fibonacci
  if flag
    assign iter - iter 1
    return
  endif
  if >= iter 10
    funccall Meta_return_offers
    return "420"
  endif

  assign sum + i1 i2
  assign i1 i2
  assign i2 sum
  funccall print sum
  assign iter + iter 1
  funccall fibonacci
endfunc


func unused
endfunc''',
'''func main        # our main function
    funccall print "Enter a number:"
    assign str_val "20"
    funccall strtoint str_val
    assign n result
    funccall factorial
    funccall print result
    if == result 6
        funccall print "you entered 3"
    else 
        funccall print "you did not enter 3"
        if == result 479001600
            funccall print "you entered 12 instead"
        else
            funccall print "you didn't enter 12 either"
        endif
    endif  
    # funccall print "this shouldn't print"
endfunc

func factorial   # compute a factorial
    assign f 1
    while > n 1
        assign f * f n
        assign n - n 1
    endwhile
    return f
endfunc''',
'''func main
 assign n 5
 if > n 1
  assign m 10
 endif
 if < m 5
  assign m n
 else
  assign n m
 endif
 funccall print "n: " n
 funccall print "m: " m
endfunc''',

'''func main
  assign i 0
  while < i 2 
    funccall print "Outer: " i
    assign j 3 
    while > j 0
      if < j 2
        return
      endif
      funccall print "Inner: " j
      assign j - j 1
    endwhile
    funccall print "Outer end: " i
    assign i + i 1
  endwhile
endfunc''',

'''func reverseme
  assign reversed_num 0
  while != num 0
    assign digit % num 10
    assign reversed_num + * reversed_num 10 digit
    assign num / num 10
  endwhile
endfunc

func main
  assign num 100
  funccall reverseme
  funccall print reversed_num
endfunc
''',
'''
func main
  assign i 0
  if False
    funccall print non_valid_name
  endif
  funccall print "This code should not error"
endfunc


''',
'''
func main
  assign s "hello ' world"
  funccall print s

  # comment 
  # funccall print "this should not print"

endfunc
''',
'''
func main
  # testing comments
  assign i 0
  assign test 5#comment 1 2 3 4 5
  assign test2 True#comment remove this comment
  funccall print test
  funccall print test2
  assign result "hello "
  funccall print result "world"#"another comment"
endfunc
''',
'''#make sure we don't prematurely initialize "result"
func main
    assign v1 result
endfunc''',
'''
func main
  funccall print 5 5
  funccall print 5 -5
endfunc
''',
'''
func main
  if True
    funccall print "this should print1"
  else
    funccall print "this should not print1"
  endif
  if False
    funccall print "this should not print2"
  else
    funccall print "this should print2"
  endif
endfunc
''',
'''
func main
  assign s "         -12345        "
  funccall strtoint s
  funccall print result
endfunc
''',
'''
func main
  funccall print "this should fail halfway through"
  assign "k" 3
  funccall print k
  funccall print "this should not print"
endfunc
''',
'''
 func main
     assign i 0
     while < i 10
          assign i + i 1
     endwhile
     funccall print "i: " i
     funccall print "this is just to make sure that weirdly indented code doesn't break"
     funccall test
 endfunc

       func test
           funccall print "wonky indent"
       endfunc
''',
'''



                              func bar
                                funccall print "bar"
                              endfunc







func main#shit
  funccall foo#fat shit
  funccall bar#barshit
  funccall print "defining a func name as '1341545&_+_+*&*^%(*)' should work since it's never called"
  funccall print "having syntax errors in an uncalled function should not cause errors"
  assign var strtoint "1" 
endfunc



func foo
  funccall print "foo"
endfunc




func 1341545&_+_+*&*^%(*)
  assign !@#$$%^&*^%&(__+^#&^%%&#%@&(*$%)) 45245 jhfdjhty7 6j7ryd
  funccall print "this function shouldn't error since it's not called"
endfunc
''',
'''
func main
  funccall print "tests wide spacing between tokens"
  assign                              fdf                                                         456
  funccall           print                                           fdf
endfunc
''',

]
