from summarizer import summarize

text = ("Manatees are herbivores and eat over 60 different freshwater and saltwater plants."
    "Manatees inhabit the shallow, marshy coastal areas and rivers of the Caribbean Sea, the Gulf of Mexico,"
    " the Amazon basin, and West Africa.\n"
    "The main causes of death for manatees are human-related issues, such as habitat destruction and human"
    " objects. Their slow-moving, curious nature has led to violent collisions with propeller-driven boats and ships."
    " Some manatees have been found with over 50 scars on them from propeller blades. Natural causes of death include "
    "adverse temperatures, predation by crocodiles on young, and disease.")
result = summarize(text, 10)
print(result)