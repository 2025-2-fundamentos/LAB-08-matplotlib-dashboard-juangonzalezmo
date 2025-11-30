# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    ruta_csv = os.path.join("files", "input", "shipping-data.csv")
    df = pd.read_csv(ruta_csv)


    os.makedirs("docs", exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 4))
    warehouse_counts = df["Warehouse_block"].value_counts().sort_index()
    warehouse_counts.plot(kind="bar", ax=ax)
    ax.set_title("Shipments per warehouse")
    ax.set_xlabel("Warehouse block")
    ax.set_ylabel("Number of shipments")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png", dpi=120)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 4))
    mode_counts = df["Mode_of_Shipment"].value_counts()
    mode_counts.plot(kind="bar", ax=ax)
    ax.set_title("Mode of shipment")
    ax.set_xlabel("Mode")
    ax.set_ylabel("Number of shipments")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png", dpi=120)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 4))
    rating_mean = (
        df.groupby("Mode_of_Shipment")["Customer_rating"]
        .mean()
        .sort_index()
    )
    rating_mean.plot(kind="bar", ax=ax)
    ax.set_title("Average customer rating by shipment mode")
    ax.set_xlabel("Mode of shipment")
    ax.set_ylabel("Average rating")
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png", dpi=120)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df["Weight_in_gms"], bins=20, edgecolor="black")
    ax.set_title("Weight distribution")
    ax.set_xlabel("Weight (g)")
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png", dpi=120)
    plt.close(fig)


    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Shipping Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            text-align: center;
        }}
        .grid {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }}
        .panel {{
            flex: 1 1 45%;
            text-align: center;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ccc;
        }}
    </style>
</head>
<body>
    <h1>Shipping Dashboard</h1>
    <div class="grid">
        <div class="panel">
            <h2>Shipments per warehouse</h2>
            <img src="shipping_per_warehouse.png" alt="Shipments per warehouse">
        </div>
        <div class="panel">
            <h2>Mode of shipment</h2>
            <img src="mode_of_shipment.png" alt="Mode of shipment">
        </div>
        <div class="panel">
            <h2>Average customer rating</h2>
            <img src="average_customer_rating.png" alt="Average customer rating">
        </div>
        <div class="panel">
            <h2>Weight distribution</h2>
            <img src="weight_distribution.png" alt="Weight distribution">
        </div>
    </div>
</body>
</html>
"""

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)
