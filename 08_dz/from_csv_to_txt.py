import csv


def write_beatiful_information(clients: list, output_file_name: str) -> None:
    f = open(output_file_name, "w")
    for client in clients:
        f.write(client)

    f.close()


def parse_client_to_text(clients: list) -> list[str]:
    clients_info = []
    for client in clients:
        client_full_information = f"""ФИО: {client[0]}\nПол: {client[3]}\nВозраст: {client[4]}\nУстройство, с которого выполнялась покупка: {client[1]}\nБраузер: {client[2]},Сумма чека: {client[5]}\nРегион покупки: {client[6]}\n---------\n"""
        clients_info.append(client_full_information)
    
    return clients_info


def get_clients_from_csv(file_name: str) -> list:
    data = []
    with open(file_name, 'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            data.append(row)

    return data[1:]


def main():
    clients = get_clients_from_csv("web_clients_correct.csv")
    clients_info = parse_client_to_text(clients)
    write_beatiful_information(clients_info, "web_clients_correct.txt")


if __name__ == '__main__':
    main()
