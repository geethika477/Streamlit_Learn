import streamlit as sl
#Displaying logos of programmimg languages along with the links for learning materials
col = sl.columns(3)
with col[0]:
    sl.header("Python")
    sl.image("python.jpg",width=200)
    sl.link_button("Learn Python","https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")
with col[1]:
    sl.header("JavaScript")
    sl.image("js.png",width=200)
    sl.link_button("Learn JavaScript","https://www.w3schools.com/js/")
with col[2]:
    sl.header("Java")
    sl.image("java.webp")
    sl.link_button("Learn Java","https://www.w3schools.com/java/")
#--------------------------------------------------------------------------------------------------------------------------------
#tabs
tab1, tab2, tab3 = sl.tabs(["Football","Swimming","Running"])
with tab1:
    sl.header("I love Football")
    sl.video("https://www.youtube.com/watch?v=gjvOfgTz6cc")
with tab2:
    sl.header("I love Swimming")
    sl.video("https://www.youtube.com/watch?v=wrHL1igBhOg")
with tab3:
    sl.header("I love Running")
    sl.video("https://www.youtube.com/watch?v=jo_t6CbKsGo")
#--------------------------------------------------------------------------------------------------------------------------------
#Expander
t1,t2,t3 = sl.tabs(["Python","Java","JavaScript"])
with t1:
    sl.header("Python")
    sl.image("python.jpg")
    with sl.expander("See Explanation"):
        sl.write("Python is a high-level, general-purpose programming language that emphasizes code readability, simplicity, and ease-of-writing with the use of significant indentation, naming, an extensive standard library, and garbage collection. Python supports multiple programming paradigms but with an emphasis on object-oriented programming and dynamic typing.")
with t2:
    sl.header("Java")
    sl.image("java.webp") 
    with sl.expander("See Explanation"):
        sl.write("Java is a high-level, class-based, object-oriented programming language designed to be platform-independent. Its core philosophy, 'Write Once, Run Anywhere' (WORA), is achieved by compiling code into bytecode that runs on any Java Virtual Machine (JVM)")  
with t3:
    sl.header("JavaScript")
    sl.image("js.png")
    with sl.expander("See Explanation"):
        sl.write("JavaScript (JS) is a programming language and core technology of the Web, alongside HTML and CSS. Created by Brendan Eich in 1995, it is maintained by Ecma International's TC39 technical committee, with related Web APIs maintained by W3C and WHATWG. As of 2025, JavaScript is the most widely used programming language on GitHub")
#-------------------------------------------------------------------------------------------------------------------
with sl.expander("Python"):
    with sl.container(border=True):
        col1, col2 = sl.columns(2)
        with col1:
            sl.image("python.jpg",width=200)
        with col2:
            sl.write("Python is a high-level, general-purpose programming language that emphasizes code readability, simplicity, and ease-of-writing with the use of significant indentation, naming, an extensive standard library, and garbage collection. Python supports multiple programming paradigms but with an emphasis on object-oriented programming and dynamic typing.")
        sl.link_button("Learn more","https://en.wikipedia.org/wiki/Python_(programming_language)")
with sl.expander("Java"):
    with sl.container(border=True):
        col1, col2 = sl.columns(2)
        with col1:
            sl.image("java.webp",width=200)
        with col2:
            sl.write("Java is a high-level, class-based, object-oriented programming language designed to be platform-independent. Its core philosophy, 'Write Once, Run Anywhere' (WORA), is achieved by compiling code into bytecode that runs on any Java Virtual Machine (JVM)")
        sl.link_button("Learn more","https://en.wikipedia.org/wiki/Java_(programming_language)")
with sl.expander("JavaScript"):
    with sl.container(border=True):
        col1, col2 = sl.columns(2)
        with col1:
            sl.image("js.png",width=200)
        with col2:
            sl.write("JavaScript (JS) is a programming language and core technology of the Web, alongside HTML and CSS. Created by Brendan Eich in 1995, it is maintained by Ecma International's TC39 technical committee, with related Web APIs maintained by W3C and WHATWG. As of 2025, JavaScript is the most widely used programming language on GitHub")
        sl.link_button("Learn more","https://en.wikipedia.org/wiki/JavaScript")
#---------------------------------------------------------------------------------------------------------------
import time
time_input = sl.text_input("Enter the time")
b = sl.button("start")
if b:
    with sl.empty():
        for seconds in range(int(time_input)):
            sl.write(f"{seconds} seconds have passed..")
            time.sleep(1)
        sl.image("finish.AVIF",width=200)
#---------------------------------------------------------------------------------------------------------------
sl.sidebar.success("select a page")
