import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_png = buffer.getvalue()

    # print(image_png)


    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # print(image_png)

    buffer.close()

    return graph


def get_plot(_slovar):

    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))

    plt.title('Тестирую графики')

    plt.plot(_slovar.keys(), _slovar.values())


    # plt.axhline(y = 100, color='r', xmin = 0.25, linestyle='-')


    plt.xticks(rotation=45)
    plt.xlabel('Дата', fontsize=20)
    plt.ylabel('Заданий', fontsize=20)

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.tight_layout()

    graph = get_graph()

    return graph
