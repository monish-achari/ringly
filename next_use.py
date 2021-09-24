def add_subcategory(request):	
	template_name = 'admin_panel/add_subcategory_new.html'
	token_id= request.session['uid']
	all_categories = dict(db.child("ProductCategory").get(token_id).val())
	if request.method=='POST':
		name = request.POST.get('name')
		offer = request.POST.get('offer')
		description =request.POST.get('description')
		category_id = request.POST.get('category_id')
		subcategory_dict = {
		"Sub_Cat_Name":name,
		'Sub_Cat_Details':description,
		'Cat_Id':category_id,
		'Offer':offer,
		"Sub_Cat_Image_Url":request.POST.get('url')
		}
		add_data_to_table(db,token_id,subcategory_dict,"ProductSubCategory","Sub_Cat_Id","Sub_Cat_Created_Date","Sub_Cat_Modified_Date")
		# db.child('ProductSubCategory').push(subcategory_dict,token_id)
		return redirect('subcategorylist')
	return render(request, template_name,locals())



"""
    <script src="https://www.gstatic.com/firebasejs/3.7.4/firebase.js"></script>
  
   <script>
      var config = {
          
      apiKey: "AIzaSyAPTy6vrUp4PU7H205fZFkUEHs9LsoSDus",
      authDomain: "citric-proxy-241616.firebaseapp.com",
      databaseURL: "https://citric-proxy-241616.firebaseio.com",
      projectId: "citric-proxy-241616",
      storageBucket: "citric-proxy-241616.appspot.com",
      messagingSenderId: "1000975911785",
      appId: "1:1000975911785:web:a4a4007840f5501308cbf8",
      measurementId: "G-138FDLBEBE"
      
      };
      
     firebase.initializeApp(config);

     function uploadimage(){
      var storage = firebase.storage();
      var file = document.getElementById("files").files[0];
      var storageRef = storage.ref();
      var thisref = storageRef.child(file.name).put(file);
      thisref.on('state_changed',function(snapshot){
      console.log("file uplaoded succesfully");
      },
      function(error) {
      },
      function() {
      // Upload completed successfully, now we can get the download URL      
      var downloadURL = thisref.snapshot.downloadURL;
      console.log("got url");
      document.getElementById("url").value = downloadURL;
      alert("file uploaded successfully");
      });
      }

</script>

"""


ringtoneCategory:

ringtoneCategoryId:

ringtoneCreatedDate:

ringtoneDownloadCount:

ringtoneId:

ringtoneLink:

ringtoneModifiedDate:

ringtoneName:

ringtoneUsedAsAlarmToneCount:

ringtoneUsedAsContactToneCount:

ringtoneUsedAsFavourite:

ringtoneUsedCount: 