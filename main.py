import re
text = "Blondie's Big Moment (1947)"
end_index = -6  # Specify the index from the end

sliced_text = text[end_index:]
result = re.sub(r'\(|\)', '', sliced_text)
print(result)
