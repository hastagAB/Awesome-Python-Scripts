const musicContainer = document.getElementById('music-container')
const menuList = document.getElementById('menulist')

const playBtn = document.getElementById('play')
const prevBtn = document.getElementById('prev')
const nextBtn = document.getElementById('next')


const audio = document.getElementById('td-audio')
const progress = document.getElementById('progress')
const progressContainer  = document.getElementById('progress-container')
const title = document.getElementById('title')
const cover = document.getElementById('cover')
const div_id = document.getElementsByClassName('music-info')[0]
const artist = document.getElementById('artist')

// Keep track of song
let songIndex = 0;
let songs = [];
let repeat = false;
let random = false;


function appendHtml(el, str) {
    var div = document.createElement('div');
    div.innerHTML = str;
    while (div.children.length > 0) {
      el.appendChild(div.children[0]);
    }
  }

function CurrentPlaylist(){
    for(m_index=0;m_index<music_list.length;m_index++){
        var current_dir = music_list[m_index];
        var li_html = `<li data-name="${current_dir}"><a href="#"><img src="assets/cover/album_cover/${current_dir}.jpg"><span class="links_name">${current_dir}</span></a><span class="tooltip">${current_dir}</span></li>`
        appendHtml(menuList,li_html)
    }
}

CurrentPlaylist();

function randomNumber(min, max) { 
    return Math.random() * (max - min) + min;
}

// Update song details
function loadSong(song){
    title.innerText = song['title'];
    audio.src = song['f_path'];
    cover.src = song['c_path'];
    div_id.id = song["id"];
    artist.innerText = song["artist"];
}

// Play Song
function playSong(music_id){
    musicContainer.classList.add('play');
    playBtn.querySelector('i.fas').classList.remove('fa-play');
    playBtn.querySelector('i.fas').classList.add('fa-pause');

    var id_data = music_id;
    
    var q_data = document.getElementById(id_data);

    console.log(q_data);
    console.log(id_data);

    if(q_data){
        q_data.classList.add('queue-active');
    }

    audio.play()
}

function playSelectedSong(music_id){

    var qu_data = document.getElementsByClassName('list_item');
    for(qu=0;qu<qu_data.length;qu++){
        qu_data[qu].classList.remove('queue-active');
    }

    var m_id = music_id.split('q')[0];
    title.innerText = songs[m_id]['title'];
    audio.src = songs[m_id]['f_path'];
    cover.src = songs[m_id]['c_path'];
    div_id.id = songs[m_id]["id"];
    artist.innerText = songs[m_id]["artist"];
    
    pauseSong(music_id);
    playSong(music_id);
}

// Pause Song
function pauseSong(music_id){
    musicContainer.classList.remove('play');
    playBtn.querySelector('i.fas').classList.remove('fa-pause');
    playBtn.querySelector('i.fas').classList.add('fa-play');
    
    var id_data = music_id;
    
    
    var q_data = document.getElementById(id_data);

    if(q_data){
        q_data.classList.remove('queue-active');
    }

    audio.pause()

}

// Previous Song
function prevSong(){

    if(repeat){
        if(songIndex != 0){
            songIndex ++;
        }
    } else if (random){
        songIndex = parseInt(randomNumber(0,songs.length));
    }

    //remove active of the current song
    var qu_data = document.getElementsByClassName('list_item');
    for(qu=0;qu<qu_data.length;qu++){
        qu_data[qu].classList.remove('queue-active');
    }


    //take index and decrease by 1
    songIndex --;
    if(songIndex < 0){
        songIndex = songs.length - 1
    }
    loadSong(songs[songIndex])
    playSong(songIndex + 'q')
}

// Next Song
function nextSong(){

    if(repeat){
        if(songIndex != 0){
            songIndex --;
        }
    } else if (random){
        songIndex = parseInt(randomNumber(0,songs.length));
    }

    //remove active of the current song
    var qu_data = document.getElementsByClassName('list_item');
    for(qu=0;qu<qu_data.length;qu++){
        qu_data[qu].classList.remove('queue-active');
    }

    //take index and decrease by 1
    songIndex ++;
    if(songIndex > songs.length - 1){
        songIndex = 0
    }
    loadSong(songs[songIndex])
    playSong(songIndex + 'q')
}

// Update progress bar
function updateProgress(e){
    // we can get the duration and current time on song from sourceElement
    const {duration, currentTime} = e.srcElement
    const progressPercent = (currentTime / duration) * 100

    progress.style.width = `${progressPercent}%`
}

// Set Progress bar
function setProgress(e){
    const width = this.clientWidth // total width
    const clickX = e.offsetX;
    const duration = audio.duration;

    // set current time of audio to right position
    audio.currentTime  = (clickX / width) * duration;

}

function firstDefaultload(dom,playlist_name){

    pauseSong('0');
    if(playlist_name){
        var var_name = playlist_name;
    }else{
        var var_name = dom.attr('data-name');
    }
    console.log(var_name);
    
    songs = main_list[var_name];
    // Initially load song details into DOM
    loadSong(songs[songIndex],var_name);

    var nextQueue = document.getElementsByClassName('next-queue')[0]

    nextQueue.remove();
    var temp_html = '<ul class="next-queue" id="next-songs"></ul>';
    var temp_node = document.getElementsByClassName('home-section')[0];
    appendHtml(temp_node,temp_html);

    new_node = document.getElementsByClassName('next-queue')[0]

    for(m_index=0;m_index<songs.length;m_index++){
        var cover_url = songs[m_index]['c_path'];
        var music_title = songs[m_index]['title'];
        var music_artist = songs[m_index]['artist'];
        var li_html = `<li class="list_item" id="${m_index+'q'}"> <div class="thumb"><img src="${cover_url}"></div><div class="info"> <div class="title">${music_title}</div><div class="artist">${music_artist}</div></div></li>`
        appendHtml(new_node,li_html);
    }

    $(".list_item").click(function() {
        playSelectedSong(this.id);
     });

    playBtn.querySelector('i.fas').classList.remove('fa-pause');
    playBtn.querySelector('i.fas').classList.add('fa-play');
}

$('#menulist li').click(function(){
    firstDefaultload($(this),null);
});

$('#repeat').click(function(){
    if($('.repeat-i').hasClass('repeat-active')){
        $('.repeat-i').removeClass('repeat-active');
        repeat = false;
    } else {
        $('.repeat-i').addClass('repeat-active');
        repeat = true;
    }
});

$('#random').click(function(){
    if($('.random-i').hasClass('random-active')){
        $('.random-i').removeClass('random-active');
        random = false;
    } else {
        $('.random-i').addClass('random-active');
        random = true;
    }
});



// Event listeners
playBtn.addEventListener('click', ()=> {
    var music_id = div_id.id;
    //If it's playing, pause
    const isPlaying = musicContainer.classList.contains('play')
    if(isPlaying){
        pauseSong(music_id+'q');
    }else {
        playSong(music_id+'q');
    }
})


// Change song
prevBtn.addEventListener('click', prevSong)
nextBtn.addEventListener('click', nextSong)

// Time/song update event
audio.addEventListener('timeupdate', updateProgress)

// Click on progress bar
progressContainer.addEventListener('click', setProgress)

// Song ends
audio.addEventListener('ended', nextSong)


firstDefaultload(null,'default');
