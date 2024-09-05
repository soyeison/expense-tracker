def formatListResponse(expenses):
    resp_string = "ID  Date        Description  Amount  \n"
    for expense in expenses:
        create_at_date = expenses[expense].createdAt.split(" ")[0]
        format_expense = f"{expenses[expense].id}   {create_at_date}  {expenses[expense].description}         {expenses[expense].amount} \n"
        resp_string = resp_string + format_expense

    return resp_string
