import matplotlib.pyplot as plt
import csv
import requests

def plot():
    x = []
    y = []
    with open('file.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        tuplelist = []
        for row in plots:
            tuplelist.append((row[0],int(row[1])))
        tuplelist = sorted(tuplelist, key=lambda x: x[1])
        for tuple in tuplelist:
            x.append(tuple[0])
            y.append(tuple[1])

    xi = list(range(len(x)))
    new_x = [2*i for i in x]
    plt.figure(figsize=(40, 20))
    plt.bar(x, y)
    plt.title('Area by State')
    plt.xlabel('Categories')
    plt.ylabel('Area(km^2)')
    plt.xticks(xi, x, rotation = 'vertical')
    plt.tick_params(axis='x',labelsize=7)
    plt.legend()
    plt.savefig("plot.png")


def send_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxb0f0777d7d684e219a2bd51fdc2afbd6.mailgun.org/messages",
		auth=("api", "86e7c34c93e6903abf17efc8d18ab129-87c34c41-dbd7e7f2"),
        files=[("attachment", open("plot.png", "rb"))],
		data={"from": "Donald Trump <donaldtrump@upenn.edu>",
			"to": "Tushar Chawla <tusharch@umich.edu>",
			"subject": "Hello Tushar Chawla",
			"text": "Congratulations Tushar Chawla, you just sent an email with Mailgun!  You are truly awesome!"})
def main():
    plot()
    send_message()

if __name__ == "__main__":
    main()