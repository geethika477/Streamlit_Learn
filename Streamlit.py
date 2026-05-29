import streamlit as sl
sl.title("Title")
sl.header("This is a header")
sl.subheader("This is a subheader")
sl.text("This is a text")
sl.balloons()
sl.markdown("---")
sl.markdown("# Hello")
sl.markdown("## Hello")
sl.markdown("### Hello")
sl.markdown("**Hello**")
sl.markdown("*Hello*")
sl.markdown(">Hello")
c = "Print('Streamlit')"
sl.code(c)
sl.markdown("[GitHub](https://github.com/geethika477?tab=repositories)")
table = """
|ID | NAME|
|---|---|
|1 | KRITI|
|2 | SHRIYA|
"""
sl.markdown(table)
sl.markdown("This is soo funny :joy:")
j = {"a":"1,2,3","b":"5,6,7"}
sl.json(j)
t = {"Column 1":[0,1,2,3,4],"Column 2":[5,6,7,8,9]}
sl.table(t)
sl.dataframe(t)
sl.metric(label="Speed", value="70ms", delta="5.2")
sl.image("bmw.avif", caption="BMW Series")
sl.audio("Barbaad Saiyaara 320 Kbps.mp3",start_time=10)
sl.video("https://www.youtube.com/watch?v=owUSRrLkCdA&list=PLMi6KgK4_mk2rK5jD-BK5RigFIP2QSq8W&index=5")
car_types = ["bmw","toyota","ford","tata","audi","hyundai"]
inp = sl.text_input("Enter car")
click = sl.button("Check Availability")
if click==True:
    if inp.lower() in car_types:
        sl.write("Car is Available")
    else:
        sl.write("Not Available")
file_name = sl.text_input("Enter file name")
with open("Audi.avif","rb") as file:
    img_data = file.read()

btn = sl.download_button(label="Download image",data=img_data,file_name=f"{file_name}.jpeg",mime="image/jpeg")
img_lst = ["yt.png","hyena.webp"]
img_cap = ["YouTube","Hyena"]
sl.image(img_lst,width=200,caption=img_cap)
sl.subheader("Welcome to Hyena Code")
sl.link_button("Hyena","https://www.youtube.com/watch?v=S-b5Ue7V-DM")
checks = sl.columns(2)
with checks[0]:
    box1 = sl.checkbox("View images")
with checks[1]:
    box2 = sl.checkbox("view code")
if box1:
    img_lst = ["yt.png","hyena.webp"]
    img_cap = ["YouTube","Hyena"]
    sl.image(img_lst,width=200,caption=img_cap)
if box2:
    sl.code("Print('This is the Code')")
col = sl.columns(3)
with col[0]:
    toggle_img = sl.toggle("Enable Image")
with col[1]:
    toggle_vid = sl.toggle("Enable Video")
with col[2]:
    toggle_aud = sl.toggle("Enable Audio")
if toggle_img:
    sl.image("Maserati.webp")
if toggle_vid:
    sl.video("https://www.youtube.com/watch?v=owUSRrLkCdA&list=PLMi6KgK4_mk2rK5jD-BK5RigFIP2QSq8W&index=5")
if toggle_aud:
    sl.audio("Barbaad Saiyaara 320 Kbps.mp3",start_time=10)
if "disabled" not in sl.session_state:
    sl.session_state.disabled = False
sl.session_state.disabled = False
radio = sl.radio("Choose course",["JavaScript","HTML|CSS","Python"],index=None,key="visibility",disabled=sl.session_state.disabled)
if radio:
    sl.write(f"You have selected {radio} course")
    sl.session_state.disabled = True
car = sl.selectbox("Which car do you want to see?",["Audi","BMW","Maserati"],index=None)
if car=="Audi":
    sl.image("Audi.avif")
if car=="BMW":
    sl.image("bmw.avif")
if car=="Maserati":
    sl.image("Maserati.webp")
#There is also multi select to be able to select more than 1 option (just like the skills session in a website)
size = sl.slider("Size of the image",100,600)
sl.image("bmw.avif",width=size)
sl.header("Speed Calculator")
dist = sl.slider("Distance in meters",0,1000)
time = sl.slider("time in secs",1,120)
sl.write(f"Speed: {dist/time} m/s")
sl.select_slider("select slider",[0,100,200,300,400,500,600,700,800,900,1000])
first_name = sl.text_input("First Name")
last_name = sl.text_input("Last Name")
btn = sl.button("show")
if btn:
    sl.write(f"Welcome {first_name} {last_name} :grin:")
num1 = sl.number_input("First Number")
num2 = sl.number_input("Second Number")
b = sl.columns(4)
with b[0]:
    b0 = sl.button("Addition (+)",type="primary")
with b[1]:
    b1 = sl.button("Subtraction (-)",type="primary")
with b[2]:
    b2 = sl.button("Multiplication (*)",type="primary")
with b[3]:
    b3 = sl.button("Division (/)",type="primary")
if b0:
    sl.write(f"{num1+num2}")
if b1:
    sl.write(f"{num1-num2}")
if b2:
    sl.write(f"{num1*num2}")
if b3:
    sl.write(f"{num1/num2}")
text_ar = sl.text_area("Text to Analyze","",placeholder="write text...",max_chars=100)
analyze = sl.button("Analyze")
if analyze:
    lst = text_ar.split()
    sl.write(f"Number of characters typed: {len(text_ar)}. Number of words typed: {len(lst)} ")
name = sl.text_input("Name")
company = sl.text_input("Company")
import datetime as dt
start_date = sl.date_input("Starting Date",min_value=dt.date(1980,1,1),max_value=dt.date.today())
end_date = sl.date_input("Ending Date",min_value=dt.date(1980,1,1),max_value=dt.date.today())
str1 = str(start_date).split('-')
str2 = str(end_date).split('-')
d1 = dt.date(int(str1[0]),int(str1[1]),int(str1[2]))
d2 = dt.date(int(str2[0]),int(str2[1]),int(str2[2]))
if sl.button("dispaly"):
    sl.write(f"You have worked at {company} for {(d2-d1).days} days")
team1 =sl.text_input("First Team Name")
team2 =sl.text_input("Second Team Name")
time = sl.time_input("Time",value=None)
if sl.button("Showw"):
    sl.write(f"The match between {team1} and {team2} starts at {time}")
f1 = sl.file_uploader("Choose an image",accept_multiple_files=True)
f2 = sl.file_uploader("Choose a text file",accept_multiple_files=True)
for f in f1:
    sl.write(f"file name: {f.name}")
    sl.image(f"{f.name}")
for f in f2:
    sl.write(f"file name: {f.name}")
    content = f.read()
    sl.write(f"{content}")
color = sl.color_picker("Pick a colour","#000000")
sl.markdown(f"<span style = 'color:{color}'>Welcome to Streamlit</span>",unsafe_allow_html=True)
sl.write(f"Current color: {color}")
with sl.form("Your form"):
    nam = sl.text_input("Name")
    surname = sl.text_input("SurName")
    age = sl.slider("Age",0,80,25)
    start = sl.date_input("Starting Date")
    submit = sl.form_submit_button("Submit")
    if submit:
        sl.write(f"Name : {nam} {surname} Age: {age} Starting Date: {start}")

# sl.markdown("""
# <style>
# .card {
#     background-color:#49DCCE;
#     padding:20px;
#     border-radius:15px;
#     box-shadow:0px 0px 10px gray;
#     transition:0.3s;
# }

# .card:hover {
#     transform:scale(1.05);
# }
# </style>
# """, unsafe_allow_html=True)

# sl.markdown("""
# <div class="card">
# <h2>Python</h2>
# <p>I love building apps.</p>
# </div>
# """, unsafe_allow_html=True)

# ---------------------------------------------------------------

# sl.markdown("""
# <style>
# .card {
#     background-color:#49DCCE;
#     padding:20px;
#     border-radius:15px;
#     box-shadow:0px 0px 10px gray;
# }

# .btn {
#     background-color:red;
#     color:white;
#     padding:10px 20px;
#     border-radius:10px;
#     text-decoration:none;
# }
# </style>
# """, unsafe_allow_html=True)

# sl.markdown("""
# <div class="card">

# <h2>Expense Tracker</h2>

# <p>A Streamlit + SQL project.</p>

# <a class="btn" href="https://github.com/" target="_blank">
# GitHub
# </a>

# </div>
# """, unsafe_allow_html=True)

# -------------------------------------------------------------

# sl.markdown("""
# <style>

# .stApp {
#     background-color:black;
# }

# </style>
# """, unsafe_allow_html=True)
# -------------------------------------------------------------
# sl.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(
#         to right,
#         #141E30,
#         #243B55
#     );
# }

# </style>
# """, unsafe_allow_html=True)


# sl.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(
#         -45deg,
#         #0f0c29,
#         #302b63,
#         #24243e,
#         #00c6ff
#     );

#     background-size: 400% 400%;

#     animation: gradient 15s ease infinite;
# }

# @keyframes gradient {

#     0% {
#         background-position: 0% 50%;
#     }

#     50% {
#         background-position: 100% 50%;
#     }

#     100% {
#         background-position: 0% 50%;
#     }
# }

# </style>
# """, unsafe_allow_html=True)

# sl.title("Animated Portfolio")
