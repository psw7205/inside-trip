import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import folium


def make_sin_cos():
    img = io.BytesIO()
    t = np.arange(0, 2 * np.pi, 0.01)

    plt.figure(figsize=(10, 6))
    plt.plot(t, np.sin(t), lw=3, label='sin')
    plt.plot(t, np.cos(t), 'r', label='cos')
    plt.grid()
    plt.legend()
    plt.title('sin ')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return plot_url


def folium_test():
    folium_map = folium.Map(location=[37.549554, 127.074984],
                            zoom_start=17)
    return folium_map._repr_html_()
