from flask import Flask, render_template, request
import sequence_validation
import codon_optimization

app = Flask(__name__)

validator = sequence_validation.SeqValidator("DNA", True, True, 1000000)

optimizer = codon_optimization.CodonOptimizer("homo_sapiens", "escherichia_coli_K12")


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/optimize')
def optimize():
    sequence = request.json.get('data')
    if sequence is not None:
        # print(sequence)
        sequence = str(sequence).strip()
        if validator.validate(sequence):
            return optimizer.optimize(sequence, isDNA=True, returnDNA=True)

    return "THIS IS NOT A VALID DNA-SEQUENCE!"


if __name__ == '__main__':
    app.run(host='localhost', port=31415, debug=False)
