def string_splosion(str):
    return "".join([str[0:n] for n in range(0,len(str)+1)])

print string_splosion("a")
print string_splosion("\"")
print string_splosion("Raghu")
