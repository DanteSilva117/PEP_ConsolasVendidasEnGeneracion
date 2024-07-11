import matplotlib.pyplot as plt
import utils
# Chart generation function
def generate_bar_chart(labels, values, generation):
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values)
    ax.set_xlabel('Consoles')
    ax.set_xlabel(generation + ' generation')
    ax.set_ylabel('Total Systems Sold')
    ax.set_title('Total Systems Sold by Console')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Annotate bars with values
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:,}', va='bottom')  # Using thousands separator

    plt.show()