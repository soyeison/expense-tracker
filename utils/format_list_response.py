def formatListResponse(expenses):
    table = [["ID", "Date", "Description", "Amount"]]
    for expense in expenses:
        add_to_table = []
        create_at_date = expenses[expense].createdAt.split(" ")[0]
        add_to_table.append(expenses[expense].id)
        add_to_table.append(create_at_date)
        add_to_table.append(expenses[expense].description)
        add_to_table.append(expenses[expense].amount)
        table.append(add_to_table)

    column_one_with = 5
    column_two_with = 13
    column_three_with = 13
    column_four_with = 5

    string_resp = ""
    for row in table:
        string_resp = string_resp + "{:<{}} {:<{}} {:<{}} {:<{}}\n".format(
            row[0],
            column_one_with,
            row[1],
            column_two_with,
            row[2],
            column_three_with,
            row[3],
            column_four_with
        )

    return string_resp
