# model generated from supplied counterexamples from the user
userquerymodel = '''s0 -> s7 [label="5ct / OK"];
s0 -> s1 [label="10ct / OK"];
s0 -> s0 [label="mars / NOK"];
s0 -> s0 [label="snickers / NOK"];
s0 -> s0 [label="twix / NOK"];
s1 -> s6 [label="5ct / OK"];
s1 -> s2 [label="10ct / OK"];
s1 -> s0 [label="mars / OK"];
s1 -> s1 [label="snickers / NOK"];
s1 -> s1 [label="twix / NOK"];
s2 -> s3 [label="5ct / OK"];
s2 -> s8 [label="10ct / OK"];
s2 -> s1 [label="mars / OK"];
s2 -> s2 [label="snickers / NOK"];
s2 -> s7 [label="twix / OK"];
s3 -> s8 [label="5ct / OK"];
s3 -> s4 [label="10ct / OK"];
s3 -> s6 [label="mars / OK"];
s3 -> s0 [label="snickers / OK"];
s3 -> s1 [label="twix / OK"];
s4 -> s5 [label="5ct / OK"];
s4 -> s10 [label="10ct / OK"];
s4 -> s3 [label="mars / OK"];
s4 -> s1 [label="snickers / OK"];
s4 -> s2 [label="twix / OK"];
s5 -> s5 [label="5ct / NOK"];
s5 -> s5 [label="10ct / NOK"];
s5 -> s8 [label="mars / OK"];
s5 -> s6 [label="snickers / OK"];
s5 -> s3 [label="twix / OK"];
s6 -> s2 [label="5ct / OK"];
s6 -> s3 [label="10ct / OK"];
s6 -> s7 [label="mars / OK"];
s6 -> s6 [label="snickers / NOK"];
s6 -> s0 [label="twix / OK"];
s7 -> s1 [label="5ct / OK"];
s7 -> s6 [label="10ct / OK"];
s7 -> s7 [label="mars / NOK"];
s7 -> s7 [label="snickers / NOK"];
s7 -> s7 [label="twix / NOK"];
s8 -> s9 [label="5ct / OK"];
s8 -> s5 [label="10ct / OK"];
s8 -> s2 [label="mars / OK"];
s8 -> s7 [label="snickers / OK"];
s8 -> s6 [label="twix / OK"];
s9 -> s9 [label="5ct / NOK"];
s9 -> s9 [label="10ct / NOK"];
s9 -> s3 [label="mars / OK"];
s9 -> s1 [label="snickers / OK"];
s9 -> s2 [label="twix / OK"];
s10 -> s10 [label="5ct / NOK"];
s10 -> s10 [label="10ct / NOK"];
s10 -> s4 [label="mars / OK"];
s10 -> s2 [label="snickers / OK"];
s10 -> s8 [label="twix / OK"];'''

# model generated using the WpMethod testing method
wpmethod = '''s0 -> s7 [label="5ct / OK"];
s0 -> s1 [label="10ct / OK"];
s0 -> s0 [label="mars / NOK"];
s0 -> s0 [label="snickers / NOK"];
s0 -> s0 [label="twix / NOK"];
s1 -> s2 [label="5ct / OK"];
s1 -> s4 [label="10ct / OK"];
s1 -> s0 [label="mars / OK"];
s1 -> s1 [label="snickers / NOK"];
s1 -> s1 [label="twix / NOK"];
s2 -> s4 [label="5ct / OK"];
s2 -> s3 [label="10ct / OK"];
s2 -> s7 [label="mars / OK"];
s2 -> s2 [label="snickers / NOK"];
s2 -> s0 [label="twix / OK"];
s3 -> s6 [label="5ct / OK"];
s3 -> s8 [label="10ct / OK"];
s3 -> s2 [label="mars / OK"];
s3 -> s0 [label="snickers / OK"];
s3 -> s1 [label="twix / OK"];
s4 -> s3 [label="5ct / OK"];
s4 -> s6 [label="10ct / OK"];
s4 -> s1 [label="mars / OK"];
s4 -> s4 [label="snickers / NOK"];
s4 -> s7 [label="twix / OK"];
s5 -> s5 [label="5ct / NOK"];
s5 -> s5 [label="10ct / NOK"];
s5 -> s3 [label="mars / OK"];
s5 -> s1 [label="snickers / OK"];
s5 -> s4 [label="twix / OK"];
s6 -> s5 [label="5ct / OK"];
s6 -> s9 [label="10ct / OK"];
s6 -> s4 [label="mars / OK"];
s6 -> s7 [label="snickers / OK"];
s6 -> s2 [label="twix / OK"];
s7 -> s1 [label="5ct / OK"];
s7 -> s2 [label="10ct / OK"];
s7 -> s7 [label="mars / NOK"];
s7 -> s7 [label="snickers / NOK"];
s7 -> s7 [label="twix / NOK"];
s8 -> s9 [label="5ct / OK"];
s8 -> s10 [label="10ct / OK"];
s8 -> s3 [label="mars / OK"];
s8 -> s1 [label="snickers / OK"];
s8 -> s4 [label="twix / OK"];
s9 -> s9 [label="5ct / NOK"];
s9 -> s9 [label="10ct / NOK"];
s9 -> s6 [label="mars / OK"];
s9 -> s2 [label="snickers / OK"];
s9 -> s3 [label="twix / OK"];
s10 -> s10 [label="5ct / NOK"];
s10 -> s10 [label="10ct / NOK"];
s10 -> s8 [label="mars / OK"];
s10 -> s4 [label="snickers / OK"];
s10 -> s6 [label="twix / OK"];'''

# model generated using the WMethod testing method
wmethod = '''s0 -> s7 [label="5ct / OK"];
s0 -> s1 [label="10ct / OK"];
s0 -> s0 [label="mars / NOK"];
s0 -> s0 [label="snickers / NOK"];
s0 -> s0 [label="twix / NOK"];
s1 -> s2 [label="5ct / OK"];
s1 -> s4 [label="10ct / OK"];
s1 -> s0 [label="mars / OK"];
s1 -> s1 [label="snickers / NOK"];
s1 -> s1 [label="twix / NOK"];
s2 -> s4 [label="5ct / OK"];
s2 -> s3 [label="10ct / OK"];
s2 -> s7 [label="mars / OK"];
s2 -> s2 [label="snickers / NOK"];
s2 -> s0 [label="twix / OK"];
s3 -> s6 [label="5ct / OK"];
s3 -> s8 [label="10ct / OK"];
s3 -> s2 [label="mars / OK"];
s3 -> s0 [label="snickers / OK"];
s3 -> s1 [label="twix / OK"];
s4 -> s3 [label="5ct / OK"];
s4 -> s6 [label="10ct / OK"];
s4 -> s1 [label="mars / OK"];
s4 -> s4 [label="snickers / NOK"];
s4 -> s7 [label="twix / OK"];
s5 -> s5 [label="5ct / NOK"];
s5 -> s5 [label="10ct / NOK"];
s5 -> s3 [label="mars / OK"];
s5 -> s1 [label="snickers / OK"];
s5 -> s4 [label="twix / OK"];
s6 -> s5 [label="5ct / OK"];
s6 -> s9 [label="10ct / OK"];
s6 -> s4 [label="mars / OK"];
s6 -> s7 [label="snickers / OK"];
s6 -> s2 [label="twix / OK"];
s7 -> s1 [label="5ct / OK"];
s7 -> s2 [label="10ct / OK"];
s7 -> s7 [label="mars / NOK"];
s7 -> s7 [label="snickers / NOK"];
s7 -> s7 [label="twix / NOK"];
s8 -> s9 [label="5ct / OK"];
s8 -> s10 [label="10ct / OK"];
s8 -> s3 [label="mars / OK"];
s8 -> s1 [label="snickers / OK"];
s8 -> s4 [label="twix / OK"];
s9 -> s9 [label="5ct / NOK"];
s9 -> s9 [label="10ct / NOK"];
s9 -> s6 [label="mars / OK"];
s9 -> s2 [label="snickers / OK"];
s9 -> s3 [label="twix / OK"];
s10 -> s10 [label="5ct / NOK"];
s10 -> s10 [label="10ct / NOK"];
s10 -> s8 [label="mars / OK"];
s10 -> s4 [label="snickers / OK"];
s10 -> s6 [label="twix / OK"];'''

# model generated using the RandomWalk testing method
randomwalk = '''s0 -> s4 [label="5ct / OK"];
s0 -> s1 [label="10ct / OK"];
s0 -> s0 [label="mars / NOK"];
s0 -> s0 [label="snickers / NOK"];
s0 -> s0 [label="twix / NOK"];
s1 -> s2 [label="5ct / OK"];
s1 -> s5 [label="10ct / OK"];
s1 -> s0 [label="mars / OK"];
s1 -> s1 [label="snickers / NOK"];
s1 -> s1 [label="twix / NOK"];
s2 -> s5 [label="5ct / OK"];
s2 -> s3 [label="10ct / OK"];
s2 -> s4 [label="mars / OK"];
s2 -> s2 [label="snickers / NOK"];
s2 -> s0 [label="twix / OK"];
s3 -> s7 [label="5ct / OK"];
s3 -> s8 [label="10ct / OK"];
s3 -> s2 [label="mars / OK"];
s3 -> s0 [label="snickers / OK"];
s3 -> s1 [label="twix / OK"];
s4 -> s1 [label="5ct / OK"];
s4 -> s2 [label="10ct / OK"];
s4 -> s4 [label="mars / NOK"];
s4 -> s4 [label="snickers / NOK"];
s4 -> s4 [label="twix / NOK"];
s5 -> s3 [label="5ct / OK"];
s5 -> s7 [label="10ct / OK"];
s5 -> s1 [label="mars / OK"];
s5 -> s5 [label="snickers / NOK"];
s5 -> s4 [label="twix / OK"];
s6 -> s6 [label="5ct / NOK"];
s6 -> s6 [label="10ct / NOK"];
s6 -> s3 [label="mars / OK"];
s6 -> s1 [label="snickers / OK"];
s6 -> s5 [label="twix / OK"];
s7 -> s6 [label="5ct / OK"];
s7 -> s9 [label="10ct / OK"];
s7 -> s5 [label="mars / OK"];
s7 -> s4 [label="snickers / OK"];
s7 -> s2 [label="twix / OK"];
s8 -> s9 [label="5ct / OK"];
s8 -> s10 [label="10ct / OK"];
s8 -> s3 [label="mars / OK"];
s8 -> s1 [label="snickers / OK"];
s8 -> s5 [label="twix / OK"];
s9 -> s9 [label="5ct / NOK"];
s9 -> s9 [label="10ct / NOK"];
s9 -> s7 [label="mars / OK"];
s9 -> s2 [label="snickers / OK"];
s9 -> s3 [label="twix / OK"];
s10 -> s10 [label="5ct / NOK"];
s10 -> s10 [label="10ct / NOK"];
s10 -> s8 [label="mars / OK"];
s10 -> s5 [label="snickers / OK"];
s10 -> s7 [label="twix / OK"];'''

models = [wpmethod, wmethod, randomwalk]
modelnames = ["WpMethod", "WMethod", "RandomWalk"]

for i in range(0,3):
    print(F"testing {modelnames[i]} for isomorphism")
    generatedmodel = models[i]

    # helper function which fills a supplied dict with the a key value pair where the two states form the key and are mapped to the label 
    # for example the transition: "s0 -> s4 [label="5ct / OK"]:" would be {"s0s4":"[label="5ct / OK"];""}
    def fill_transition_dictionary(dict, model):
        for t in model.split('\n')[:-1]:
            elems = t.split(' ')
            dict[elems[0] + elems[2]] = elems[3:] 
        return dict

    # applied transformations to the state names to make the model isomorphicly equal to the userquerymodel
    if generatedmodel == wpmethod or generatedmodel == wmethod:
        # transformations: 4 -> 2, 2 -> 6, 6 -> 8, 8 -> 4 and 5 -> 9, 9 -> 5
        transformedmodel = generatedmodel.replace('s8','sx').replace('s6', 's8').replace('s2', 's6').replace('s4', 's2').replace('sx', 's4').replace('s5', 'sx').replace('s9', 's5').replace('sx', 's9')
    if generatedmodel == randomwalk:
        # transformations: 5 -> 2, 2 -> 6, 6 -> 9, 9 -> 5 and 4 -> 7, 7 -> 8, 8 -> 4
        transformedmodel = generatedmodel.replace('s9','sx').replace('s6', 's9').replace('s2', 's6').replace('s5', 's2').replace('sx', 's5').replace('s8', 'sx').replace('s7', 's8').replace('s4', 's7').replace('sx', 's4')

    # fill the transition dictionaries
    userdict = fill_transition_dictionary({}, userquerymodel)

    transdict = fill_transition_dictionary({}, transformedmodel)

    # make sure that the amount of transitions is equal
    if len(userdict) != len(transdict):
        print("different transition counts: no isomorphism")

    # test the transition dictionaries for equivalence no output means a perfect match and thus isomorphism

    for u in userquerymodel.split('\n')[:-1]:
        key = u.split(' ')[0] + u.split(' ')[2]
        try:
            usert =  userdict[key]
            transt = transdict[key]
            if usert != transt:
                print("transition inequality:")
                print(key)
                print(usert)
                print(transt)
        except:
            print(key)
            print("was not present in one (or both) of the dicts")


