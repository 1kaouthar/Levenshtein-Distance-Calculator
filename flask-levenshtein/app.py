from flask import Flask, request, render_template

app = Flask(__name__)

class Solution:
    def minDistance(self, string1, string2):
        distance = [[c for c in range(len(string1) + 1)] for r in range(len(string2) + 1)]
        
        for r in range(1, len(string2) + 1):
            distance[r][0] = distance[r - 1][0] + 1
        
        for r in range(1, len(string2) + 1):
            for c in range(1, len(string1) + 1):
                if string1[c - 1] == string2[r - 1]:
                    distance[r][c] = distance[r - 1][c - 1]
                else:
                    distance[r][c] = 1 + min(distance[r][c - 1], 
                                             distance[r - 1][c - 1], 
                                             distance[r - 1][c])
        
        return distance[-1][-1]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        string1 = request.form['string1']
        string2 = request.form['string2']
        solution = Solution()
        result = solution.minDistance(string1, string2)
        return render_template('index.html', result=result, string1=string1, string2=string2)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
