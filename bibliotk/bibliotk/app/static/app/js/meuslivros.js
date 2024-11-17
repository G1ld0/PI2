let currentFontSize = 16;
let currentBackgroundColor = '#ffffff';
let currentTextColor = '#000000';
let highlightedRanges = [];

function changeFontSize(amount) {
    currentFontSize += amount;
    document.getElementById('book').style.fontSize = currentFontSize + 'px';
}

function changeBackgroundColor() {
    currentBackgroundColor = currentBackgroundColor === '#ffffff' ? '#f0f0f0' : '#ffffff';
    document.getElementById('book').style.backgroundColor = currentBackgroundColor;
}

function togglePageBackground() {
    const body = document.body;
    body.style.backgroundColor = body.style.backgroundColor === 'black' ? '#f4f4f4' : 'black';
    body.style.color = body.style.color === 'white' ? '#333' : 'white';
}

function changeTextColor(color) {
    currentTextColor = color;
    document.getElementById('book').style.color = currentTextColor;
}

function markText() {
    const selection = window.getSelection();
    if (selection.rangeCount > 0) {
        const range = selection.getRangeAt(0);
        const span = document.createElement('span');
        span.className = 'highlight';
        range.surroundContents(span);
        highlightedRanges.push(range);
    }
}

function undoMark() {
    if (highlightedRanges.length > 0) {
        const range = highlightedRanges.pop();
        range.surroundContents(document.createTextNode(range.toString()));
    }
}

function downloadText() {
    const text = document.getElementById('book').textContent;
    const blob = new Blob([text], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'livro.txt';
    a.click();
}