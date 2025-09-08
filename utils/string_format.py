from datetime import datetime


# Converte para date se vier string
def to_date(value):
    if value:
        return datetime.strptime(value, "%Y-%m-%d").date()
    return None


def to_iso(value: str):
    if value:
        return datetime.fromisoformat(f'{value} 00:00:00')
    return None


if __name__ == "__main__":
    # print(to_date("2023-10-05"))
    print(to_iso("2023-10-05 00:00:00"))
