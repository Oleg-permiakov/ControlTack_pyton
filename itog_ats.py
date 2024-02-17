import random

lst = ["robot"] * 10
lst += ["human"] * 10
b = random.shuffle(lst)
data = pd.DataFrame({"whoAmi":lst})
data.head()
data.loc[data["whoAmi"]=="robot", "all_robots"] = 1
data.loc[data["whoAmi"]=="human", "all_robots"] = 0
data.loc[data["whoAmi"]=="robot", "all_human"] = 0
data.loc[data["whoAmi"]=="human", "all_human"] = 1