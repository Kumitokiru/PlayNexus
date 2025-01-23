document.querySelector('.sbrbtn').addEventListener('click', function () {
    let searchQuery = document.querySelector('.srchbr').value;
    alert('Searching for: ' + searchQuery);
});

document.querySelector('.mscbtn').addEventListener('click', function () {
   
});



document.querySelector('.plystbtn').addEventListener('click', function () {
   
});

document.querySelector('.vdsbtn').addEventListener('click', function () {
    
});

document.querySelector('.sttngsbtn').addEventListener('click', function () {
    
});

document.querySelector('.addmscbtn').style.display = 'none';

document.querySelector('.mscbtn').addEventListener('click', function () {
    document.querySelector('.addmscbtn').style.display = 'block';
});

