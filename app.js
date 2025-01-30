fetch("BookCsv.csv")
  .then(response => response.text())
  .then(csvText => {
    const parsedData = Papa.parse(csvText, {
      header: true,
      skipEmptyLines: true
    });

    console.log("변환된 데이터: ", parsedData.data);
    displayData(parsedData.data)
  })
.catch(error => console.error("오류 발생: ", error))

function displayData(dataArray) {
  const output = document.getElementById("output");
  output.textContent = JSON.stringfy(dataArray, null, 2);
}
