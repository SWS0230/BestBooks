fetch('BookCsv.csv') // 현재 디렉토리에서 CSV 파일 가져오기
    .then(response => response.text()) // 텍스트 변환
    .then(csvText => {
        parseCSV(csvText); // CSV 변환 함수 호출
    })
    .catch(error => console.error("❌ CSV 파일을 불러오는 중 오류 발생:", error));

function parseCSV(csvText) {
    const rows = csvText.trim().split("\n").map(row => row.split(",")); // CSV 데이터를 배열로 변환

    if (rows.length < 2) {
        console.error("❌ CSV 데이터가 부족합니다.");
        return;
    }

    const headers = rows[0]; // 첫 번째 줄을 헤더로 사용
    const data = rows.slice(1); // 나머지는 데이터

    displayTable(headers, data);
}

function displayTable(headers, data) {
    const headerRow = document.getElementById("table-header");
    const tableBody = document.getElementById("table-body");

    // 헤더 추가
    headerRow.innerHTML = headers.map(header => `<th>${header}</th>`).join("");

    // 데이터 추가
    tableBody.innerHTML = data.map(row => 
        `<tr>${row.map(cell => `<td>${cell}</td>`).join("")}</tr>`
    ).join("");
}
