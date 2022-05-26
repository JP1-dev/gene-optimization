
const hemoglobin = "ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAA";

function start() {
  document.getElementById("helloDiv").style.visibility = 'hidden';
  document.getElementById("main").style.visibility = 'visible';
}

function optimize() {

  const Http = new XMLHttpRequest();
  const url = 'http://localhost:31415/optimize';
  Http.open("POST", url);
  Http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

  const data = document.getElementById("sequenceInput").value;

  Http.send(JSON.stringify({'data': data}));

  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
    document.getElementById("sequenceOutput").value = Http.responseText;
  }
}

function example() {
  document.getElementById("sequenceInput").value = hemoglobin;
}
