var pics = ['PPT_1.png','PPT_2.png','PPT_3.png','PPT_4.png','PPT_5.png','PPT_6.png']

var numImage;
numImage = 0;

function PreviousImage() {
  if (numImage>=1) {
    numImage -=1
  }else {
    numImage=0
  }
  afficherImage(numImage)
}
function NextImage() {
  if (numImage<pics.length) {
    numImage +=1
  }else {
    numImage=pics.length
  }
  afficherImage(numImage)
}

function afficherImage(num) {
  fileName = 'images/'+pics[num]
  document.getElementById("affichagePpt").scr={{ url_for('static', filename='fileName') }}
}
