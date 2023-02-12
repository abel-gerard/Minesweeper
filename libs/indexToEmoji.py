def indexToEmoji(number):
    number = list(str(number))
    ret = ""
    
    for num in number:
        match num:
            case "0": ret += "0️⃣ "
            case "1": ret += "1️⃣ "
            case "2": ret += "2️⃣ "
            case "3": ret += "3️⃣ "
            case "4": ret += "4️⃣ "
            case "5": ret += "5️⃣ "
            case "6": ret += "6️⃣ "
            case "7": ret += "7️⃣ "
            case "8": ret += "8️⃣ "
            case "9": ret += "9️⃣ "
            case   _: ret += " "
        
    return ret

# print(indexToEmoji(24953))