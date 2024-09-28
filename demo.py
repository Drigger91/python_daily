print("--Hello--")

# for i in range(5):
#     print("i is: ", i);

# for i in range(5): 
#     for j in range(5):
#         print(i * j);

# a = {};
# a["xyz"] = "hello";

# for i in a :
#     print("value for key {} is {}".format(i, a[i]));
    
course = "lets say something"
copy_course = course[:];
copy_course += " added";

# print("{} (copy ->) {}".format(course, copy_course))

if ('lets ' in course) :
    print("it is a substring")


i = 1;
while i < 5:
    print('*' * i);
    i += 1;
x = [];
for i in range(5):
    x.append(i * i);
print(x);
x.extend([88]);
x.extend({99})
"""
by default it'll extract keys from dict
"""
x.extend({
    'a' : 90
})
print(x)
