# =============================================================
# --------------------------- args ----------------------------
# =============================================================

def addition(a, *args):
    sum = a

    for arg in args:
        sum = sum + arg

    return sum


print(addition(1, 1, 1, 1, 1))

print("=======================================================")

# =============================================================
# -------------------------- kwargs ---------------------------
# =============================================================

def userInformation(**kwargs):

    for key, value in kwargs.items():
        print(key, value)


userInformation(
    name="Shivam",
    age=21,
    rollNo=2332363,
    isGraduate=True
)


"""
==============================================================
Difference Between *args and **kwargs
==============================================================

*args
------
- *args multiple positional arguments receive karta hai.
- Ye arguments tuple ke form me store hote hain.
- Jab hume nahi pata hota kitne arguments aayenge,
  tab *args use karte hain.

Example:
addition(1, 2, 3, 4)

Yaha:
a = 1
args = (2, 3, 4)

--------------------------------------------------------------

**kwargs
---------
- **kwargs multiple keyword arguments receive karta hai.
- Ye arguments dictionary ke form me store hote hain.
- Har value ek key ke saath pass hoti hai.

Example:
userInformation(name="Shivam", age=21)

Yaha:
kwargs = {
    "name": "Shivam",
    "age": 21
}

--------------------------------------------------------------

Difference
----------
*args   -> Tuple (Positional Arguments)
**kwargs -> Dictionary (Keyword Arguments)

Use:
- *args jab number of positional arguments fix na ho.
- **kwargs jab keyword arguments fix na ho.

Best Practice:
Agar function dono types ke arguments receive kare,
to signature aise likhte hain:

def demo(*args, **kwargs):
    pass
"""