// document.getElementById('upload-csv').addEventListener('change', function(event) {
//   const file = event.target.files[0];
//   if (file) {
//     Papa.parse(file, {
//       header: true, // CSV 첫 줄을 헤더로 간주
//       skipEmptyLines: true, // 빈 줄 무시
//       complete: function(results) {
//         console.log("Parsed Data: ", results.data);
//         displayData(results.data);
//       }
//     });
//   }
// });

// function displayData(data) {
//   const output = document.getElementById('output');
//   output.textContent = JSON.stringify(data, null, 2);
// }

document.getElementById('upload-csv').addEventListener('change', function(event) {
  const file = event.target.files[0];

  if (file) {
    Papa.parse(file, {
      header: true, // 첫 줄을 key 값으로 변환 (JSON 배열 형태로 반환)
      skipEmptyLines: true, // 빈 줄 무시
      complete: function(results) {
        const dataArray = results.data; // CSV 데이터를 배열로 변환
        console.log("📌 변환된 배열:", dataArray);
        processData(dataArray); // 배열 데이터 활용 함수 호출
      }
    });
  }
});

function processData(dataArray) {
  const bookList = document.getElementById('book-list');
  bookList.innerHTML = ""; // 기존 리스트 초기화

  dataArray.forEach(book => {
    const listItem = document.createElement('li');
    listItem.textContent = `${book.Title} - ${book.Author} (${book.Year})`;
    bookList.appendChild(listItem);
  });
}
