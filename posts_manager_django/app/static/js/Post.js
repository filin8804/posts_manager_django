var Post = function(){

  var text = "";
  var author = "";
  var categoryId = null;
  
  this.fillWithFormOnPage = function(){
	  this.text = document.getElementById("text").value;
	  this.author = document.getElementById("author").value;
	  this.categoryId = document.getElementById("category").value;
  }
  
  this.isValid = function(){
	  return this.text.length > 0 && this.author.length > 0 && this.categoryId != null;
  }
  
  this.add = function(){
	  if(this.isValid()){
		  Post.element_loader.style.display = 'block';		  
		  var xhr = new XMLHttpRequest();
		  xhr.open("POST", Post.URL_ADD, true);
		  xhr.setRequestHeader('Content-Type', 'application/json');
		  xhr.onreadystatechange = function() {
			  	Post.element_loader.style.display = 'none';
			    if(xhr.readyState == 4 && xhr.status == 200) { //successful response
			        alert(http.responseText);
			    }
		  }
		  xhr.send(JSON.stringify({
		      post: this
		  }));
	  }else{
		  this.printAddStatusMessage(Post.MESSAGE_NOT_VALID, false);
	  }
  }
  
  this.printAddStatusMessage = function(message, isGood){
	  var spanClass = isGood ? "msg-good" : "msg-bad";
	  var html = "<div id='addStatusMessage' class='" + spanClass + "'>" + message + "</div>";
	  document.getElementById('addStatusMessages').innerHTML += html;
  }
  
}

Post.URL_ADD = "/post/add";
Post.MESSAGE_NOT_VALID = "Post is not valid. Please check the form."
Post.MESSAGE_ADDED = "Post added."

Post.element_loader = document.getElementById("postLoader");

Post.bindUIEvents = function(){
	var btnAddPost = document.getElementById("btnAddPost");
	if(btnAddPost != null){
		btnAddPost.addEventListener("click", function(){
			var post = new Post();
			post.fillWithFormOnPage();
			post.add();
		});
	}
}


