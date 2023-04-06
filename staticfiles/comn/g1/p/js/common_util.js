/*
var protocol = document.location.protocol;
var hostname = document.location.hostname;
var port = document.location.port;
var pathname = document.location.pathname;
var newUrl = "";

if(protocol=="http:") {
  newUrl = "https://" + hostname + ":443" + pathname;
  document.location.href = newUrl;
}
*/	
	function CheckPassword(ObjUserID, ObjUserPassWord, objUserPassWordRe) {
		return CheckPassword2Composite(ObjUserID, ObjUserPassWord, objUserPassWordRe)
	}
	
	/**
	 * 비밀번호 확인
	 * 두가지 조합으로 확인
	 */
	function CheckPassword2Composite(ObjUserID, ObjUserPassWord, objUserPassWordRe) {
	    if(ObjUserPassWord.value != objUserPassWordRe.value) {
	        alert("입력하신 비밀번호와 비밀번호확인이 일치하지 않습니다");
	        return false;
	    }
		
	    if(ObjUserPassWord.value.length<10) {
	        alert("비밀번호는 영문자, 숫자의 조합으로 10~16자리로 입력해주세요.");
	        return false;
	    }
	    
		var chk_num = ObjUserPassWord.value.search(/[0-9]/); 
		var chk_eng = ObjUserPassWord.value.search(/[a-zA-Z]/); 
		var chk_special = ObjUserPassWord.value.search(/[!,@,#,$,%,^,&,*,?,_,~]/);
		
	  if(chk_num <0 || chk_eng<0) {
	  	alert("비밀번호는 영문자, 숫자의 조합으로 10~16자리로 입력해주세요.");
	    return false;
	  }
	  
		if(ObjUserPassWord.value.indexOf(ObjUserID.value) != -1) {
			alert("비밀번호에 아이디를 사용할 수 없습니다.");
			return false;
		}
		
	  var SamePass_0 = 0; //동일문자 카운트
	  var SamePass_1 = 0; //연속성(+) 카운드
	  var SamePass_2 = 0; //연속성(-) 카운드
	  
	  var chr_pass_0;
	  var chr_pass_1;
	  var chr_pass_2;
	    
	  for(var i=0; i < ObjUserPassWord.value.length; i++) {
	    chr_pass_0 = ObjUserPassWord.value.charAt(i);
	    chr_pass_1 = ObjUserPassWord.value.charAt(i+1);
	    
	    //동일문자 카운트
	    if(chr_pass_0 == chr_pass_1) {
	        SamePass_0 = SamePass_0 + 1
	    }
	    
	    chr_pass_2 = ObjUserPassWord.value.charAt(i+2);
		
	    //연속성(+) 카운드
			if(chr_pass_0.charCodeAt(0) - chr_pass_1.charCodeAt(0) == 1 && chr_pass_1.charCodeAt(0) - chr_pass_2.charCodeAt(0) == 1) {
	        SamePass_1 = SamePass_1 + 1
	    }
	      
	    //연속성(-) 카운드
	    if(chr_pass_0.charCodeAt(0) - chr_pass_1.charCodeAt(0) == -1 && chr_pass_1.charCodeAt(0) - chr_pass_2.charCodeAt(0) == -1) {
	        SamePass_2 = SamePass_2 + 1
	    }
		}
	    
		if(SamePass_0 > 1) {
	    alert("동일문자를 3번 이상 사용할 수 없습니다.");
	    return false;
	  }
	   
	  if(SamePass_1 > 1 || SamePass_2 > 1 ) {
	      alert("연속된 문자열(123 또는 321, abc, cba 등)을\n 3자 이상 사용 할 수 없습니다.");
	      return false;
	  }
	 	return true;
	}
	
	/**
	 * 비밀번호 확인
	 * 세가지 조합으로 확인
	 */
	function CheckPassword3Composite(ObjUserID, ObjUserPassWord, objUserPassWordRe) {
	    if(ObjUserPassWord.value != objUserPassWordRe.value) {
	        alert("입력하신 비밀번호와 비밀번호확인이 일치하지 않습니다");
	        return false;
	    }
		
	    if(ObjUserPassWord.value.length<8) {
	        alert("비밀번호는 영문자, 숫자, 특수문자의 조합으로 8~16자리로 입력해주세요.");
	        return false;
	    }
	
		var chk_num = ObjUserPassWord.value.search(/[0-9]/); 
		var chk_eng = ObjUserPassWord.value.search(/[a-zA-Z]/); 
		var chk_special = ObjUserPassWord.value.search(/[!,@,#,$,%,^,&,*,?,_,~]/);
		//alert(chk_num + "/" + chk_eng + "/" + chk_special);
		
	  //if(chk_num <0 || chk_eng<0 || chk_special<0) {
	  if(chk_num <0 || chk_eng<0) {
	  	alert("비밀번호는 숫자, 영문자, 특수문자를 반드시 포함하여 8~16자리로 입력해주세요.");
	    return false;
	  }

	  // 비밀번호 특수문자
	  var allowCharPw = "!@#$%^&*?_~";
	  var val = ObjUserPassWord.value;
		for(var idx=0; idx<val.length; idx++) {
			var cur = val.substring(idx, idx+1);
			//console.log(cur);

			if(allowCharPw.indexOf(cur)==-1) {
				alert("비밀번호에 사용할 수 없는 문자가 입력되었습니다. 사용할 수 있는 문자는 숫자, 영어 대/소문자, 특수문자를 조합하여 입력해 주세요.\n\n특수문자의 경우 ! @ # $ % ^ & * ? _ ~ 만 사용가능합니다.");
				return false;
			}
		}
	    
		if(ObjUserPassWord.value.indexOf(ObjUserID.value) != -1) {
			alert("비밀번호에 아이디를 사용할 수 없습니다.");
			return false;
		}
		
	  var SamePass_0 = 0; //동일문자 카운트
	  var SamePass_1 = 0; //연속성(+) 카운드
	  var SamePass_2 = 0; //연속성(-) 카운드
	  
	  var chr_pass_0;
	  var chr_pass_1;
	  var chr_pass_2;
	  
	  for(var i=0; i < ObjUserPassWord.value.length; i++)
	  {
	    chr_pass_0 = ObjUserPassWord.value.charAt(i);
	    chr_pass_1 = ObjUserPassWord.value.charAt(i+1);
	    
	    //동일문자 카운트
	    if(chr_pass_0 == chr_pass_1) {
	        SamePass_0 = SamePass_0 + 1
	    }
	   	
	    chr_pass_2 = ObjUserPassWord.value.charAt(i+2);
	    
	    //연속성(+) 카운드
			if(chr_pass_0.charCodeAt(0) - chr_pass_1.charCodeAt(0) == 1 && chr_pass_1.charCodeAt(0) - chr_pass_2.charCodeAt(0) == 1) {
	        SamePass_1 = SamePass_1 + 1
	    }
	    
	    //연속성(-) 카운드
	    if(chr_pass_0.charCodeAt(0) - chr_pass_1.charCodeAt(0) == -1 && chr_pass_1.charCodeAt(0) - chr_pass_2.charCodeAt(0) == -1) {
	        SamePass_2 = SamePass_2 + 1
	    }
	  }
	    
	  if(SamePass_0 > 1) {
	      alert("동일문자를 3번 이상 사용할 수 없습니다.");
	      return false;
	  }
	   
	  if(SamePass_1 > 1 || SamePass_2 > 1 ) {
	      alert("연속된 문자열(123 또는 321, abc, cba 등)을\n 3자 이상 사용 할 수 없습니다.");
	      return false;
	  }
	 	return true;
	}

	/**
	 * =====================================================
	 * 문자열 값이 유효한 값인지 검사한다.
	 * @ Parameter
	 *	val : 검사할 문자열
	 * @ Return
	 *	boolean : true(유효한 문자열) / false(유효하지 않은 문자열)
	 * =====================================================
	 */
	function isValidStr(val) {
		if(val!=undefined && val!=null && String(val).length>0 && val!="undefined" && val!="null")
			return true;
		else
			return false;
	}

	/**
	 * =====================================================
	 * 유효한 오브젝트인지 검사한다.
	 * @ Parameter
	 *	val : 검사할 객체
	 * @ Return
	 *	boolean : true(유효한 객체) / false(유효하지 않은 객체)
	 * =====================================================
	 */
	function isValidObj(obj) {
		if(obj!=undefined && obj!=null)
			return true;
		else
			return false;
	}


	/**
	 * =====================================================
	 * Object를 찾아서 리턴한다.
	 * @ Parameter
	 *	objName : 객체 아이디
	 * @ Return
	 *	Object : ID가 일치하는 Object
	 * =====================================================
	 */
	function findObject(objName) {
		var obj = document.getElementById(objName);
		//if(obj==null || obj==undefined)
		//	alert(objName);

		return obj;
	}

	/**
	 * =====================================================
	 * Select Box의 Option을 삭제
	 * @ Parameter
	 *	e : select
	 * @ Return
	 *	void
	 * =====================================================
	 */
	function removeAll(e){
	  for(var i = 0, limit = e.options.length; i < limit - 1; ++i){
	      e.remove(1);
	  }
	}

	/**
	 * =====================================================
	 * Select 박스에 특정값을 찾아 선택된 상태로 처리
	 * =====================================================
	 */
	function setSelectValue(obj, val) {
		if(obj==null || obj==undefined) {
			alert("Object is null");
			return;
		}

		for(var idx=0; idx<obj.options.length; idx++) {
			if(obj.options[idx].value==val) {
				obj.options.selectedIndex = idx;
				break;
			}
		}
	}

	/**
	 * =====================================================
	 * Select 박스에 선택된 값을 리턴
	 * =====================================================
	 */
	function getSelectValue(obj) {
		var retVal = "";

		if(obj==null || obj==undefined) {
			alert("Object is null");
			return null;
		}

		for(var idx=0; idx<obj.options.length; idx++) {
			if(obj.options[idx].selected) {
				retVal = obj.options[idx].value;
				break;
			}
		}
		return retVal;
	}

	/**
	 * =====================================================
	 * Select 박스에 선택된 텍스트를 리턴
	 * =====================================================
	 */
	function getSelectText(obj) {
		var retVal = "";

		if(obj==null || obj==undefined) {
			alert("Object is null");
			return null;
		}

		for(var idx=0; idx<obj.options.length; idx++) {
			if(obj.options[idx].selected) {
				retVal = obj.options[idx].text;
				break;
			}
		}
		return retVal;
	}

	/**
	 * =====================================================
	 * Select 박스에 선택된 텍스트를 리턴
	 * =====================================================
	 */
	function getSelectLabel(obj) {
		var retVal = "";

		if(obj==null || obj==undefined) {
			alert("Object is null");
			return null;
		}

		for(var idx=0; idx<obj.options.length; idx++) {
			if(obj.options[idx].selected) {
				retVal = obj.options[idx].label;
				break;
			}
		}
		return retVal;
	}

	/**
	 * =====================================================
	 * Input 생성
	 * @ Parameter
	 *	oType : Input type(hidden, text ...)
	 *	oName : Input 이름
	 *	oValue : Input Object에 셋팅될 초기값
	 * =====================================================
	 */
	function createInput(oType, oName, oValue) {
		var obj = document.createElement("input");
		obj.setAttribute("type", oType);
		obj.setAttribute("class", "form2");
		obj.setAttribute("name", oName);
		obj.setAttribute("id", oName);
		obj.setAttribute("value", oValue);


		return obj;
	}

	/**
	 * =====================================================
	 * 회원이름이 유효한지 확인한다.
	 * 이 함수는 본인 인증을 사용하므로 더이상 사용하지 않음
	 * =====================================================
	 */
	function isValid_name(str) {
		str = str.replace(/(^\s*)|(\s*$)/g, "");
		if( str == '' ){
			alert("이름을 입력하세요.");
			return false;
		}

		var retVal = checkSpace( str );

		if( retVal ){
			alert("이름은 띄어쓰기 없이 입력하세요.");
			return false;
		}

		if( !isHangul(str) ) {
			alert("이름을 정확하게 입력해 주세요.");
			return false;
		}
		if( str.length > 10 ) {
			alert("이름은 10자까지만 사용할 수 있습니다.");
			return false;
		}

		return true;
	}

	/**
	 * =====================================================
	 * 한글인지 확인
	 * =====================================================
	 */
	function isHangul(s){
		var len;
		len = s.length;

		for (var i = 0; i < len; i++)  {
			if (s.charCodeAt(i) != 32 && (s.charCodeAt(i) < 44032 || s.charCodeAt(i) > 55203))
			return false;
		}

		return true;
	}

	/**
	 * =====================================================
	 * 비밀번호 유효성 검사
	 * =====================================================
	 */
	function isValid_passwd(str) {
		var cnt = 0;

		if( str == ""){
			alert("비밀번호를 입력하세요.");
			return false;
		}

		/* check whether input value is included space or not  */
		var retVal = checkSpace( str );
		if( retVal ) {
			alert("비밀번호는 공백없이 입력해 주세요.");
			return false;
		}
		if( str.length < 6 ){
			alert("비밀번호는 6~16자의 영문 대소문자와 숫자, 특수문자를 사용할 수 있습니다.");
			return false;
		}

		for( var i=0; i < str.length; ++i){
			if( str.charAt(0) == str.substring( i, i+1 ) ) ++cnt;
		}
		if( cnt == str.length ) {
			alert("안전도가 너무 낮습니다. 다른 비밀번호를 입력해 주세요.");
			return false;
		}

		var isPW = /^[A-Za-z0-9`\-=\\\[\];',\./~!@#\$%\^&\*\(\)_\+|\{\}:"<>\?]{6,16}$/;
		if( !isPW.test(str) ) {
			alert("비밀번호는 6~16자의 영문 대소문자와 숫자, 특수문자를 사용할 수 있습니다.");
			return false;
		}
		return true;
	}

	/**
	 * =====================================================
	 * 이메일 유효성 검사
	 * =====================================================
	 */
	function isValid_email(str){
		/* check whether input value is included space or not  */
		if(str == ""){
			alert("이메일 주소를 입력해 주세요.");
			return false;
		}
		var retVal = checkSpace( str );
		if( retVal ) {
			alert("이메일주소를 정확하게 입력해 주세요..");
			return false;
		}

		if( -1 == str.indexOf('.') ) {
			alert("이메일 주소를 정확하게 입력해 주세요.");
			return false;
		}

		/* checkFormat */
		var isEmail = /[-!#$%&'*+\/^_~{}|0-9a-zA-Z]+(\.[-!#$%&'*+\/^_~{}|0-9a-zA-Z]+)*@[-!#$%&'*+\/^_~{}|0-9a-zA-Z]+(\.[-!#$%&'*+\/^_~{}|0-9a-zA-Z]+)*/;
		if( !isEmail.test(str) ) {
			alert("이메일 주소를 정확하게 입력해 주세요.");
			return false;
		}
		if( str.length > 60 ) {
			alert("이메일 주소를 정확하게 입력해 주세요.");
			return false;
		}

		return true;
	}

	/**
	 * =====================================================
	 * 이메일 마스킹 1
	 * =====================================================
	 */
	function maskEmail(email, firstLen, lastLen) {
		//alert(email + "/" + firstLen + "/" + lastLen);

		if(email==null || email.length==0)
			return "";

		var tmpA = email.split("@");

		if(tmpA.length < 2)
			return email;

		var email_id = tmpA[0];
		var email_host = tmpA[1];

		var dispLen = firstLen + lastLen;
		var idLen = email_id==null ? 0 : email_id.length;

		if(idLen <= dispLen)
			return email;

		//alert(email_id);


		var retStr = "";
		var prefix = email_id.substring(0, firstLen);
		var surfix = email_id.substring(email_id.length-lastLen, email_id.length);
		var remain = email_id.length - (firstLen + lastLen);

		//alert(prefix + "/" + surfix + "/"  + remain);
		for(var idx=0; idx<remain; idx++) {
			retStr += "*";
		}

		retStr = prefix + retStr + surfix + "@" + email_host;
		//alert(retStr);

		return retStr;
	}

	/**
	 * =====================================================
	 * 이메일 마스킹 2
	 * =====================================================
	 */
	function maskEmail2(email, firstLen, lastLen) {
		//alert(email + "/" + firstLen + "/" + lastLen);

		if(email==null || email.length==0)
			return "";

		var tmpA = email.split("@");

		if(tmpA.length < 2)
			return email;

		var email_id = tmpA[0];
		var email_host = tmpA[1];

		var dispLen = firstLen + lastLen;
		var idLen = email_id==null ? 0 : email_id.length;

		if(idLen <= dispLen)
			return email;

		//alert(email_id);


		var retStr = "";
		var prefix = email_id.substring(0, firstLen);
		var surfix = email_id.substring(email_id.length-lastLen, email_id.length);
		var remain = email_id.length - (firstLen + lastLen);

		//alert(prefix + "/" + surfix + "/"  + remain);
		for(var idx=0; idx<remain; idx++) {
			retStr += "*";
		}

		//retStr = prefix + retStr + surfix + "@" + email_host;
		//alert(retStr);

		var maskHost = "";
		var hostA = email_host.split(".");
		if(hostA==null || hostA.length<2)
			return email;

		for(var idx=0; idx<hostA.length; idx++) {
			var tmp = hostA[idx];
			var len = tmp.length;

			if(idx==0) {
				maskHost += tmp.substring(0,1);
				for(var sidx=1; sidx<tmp.length; sidx++) {
					maskHost += "*";
				}
			} else if(idx==hostA.length-1) {
				maskHost += tmp;
			} else {
				for(var sidx=0; sidx<tmp.length; sidx++) {
					maskHost += "*";
				}
			}
			if(idx<hostA.length-1)
				maskHost += ".";
		}

		retStr = prefix + retStr + surfix + "@" + maskHost;
		//alert(retStr);

		return retStr;
	}

	/**
	 * =====================================================
	 * 핸드폰 마스킹
	 * =====================================================
	 */
	function maskMobile(mobile) {

		mobile = mobile.split("-").join("").split(" ").join("");

		if(mobile==null || mobile.length==0 )
			return "";

		if(mobile.length < 10)
			return mobile;

		var retStr = "";
		var str1 = mobile.substring(0, 3);
		var str2 = mobile.substring(3, (mobile.length-4));
		var str3 = mobile.substring(mobile.length-4, mobile.length);

		//alert(str1 + "/" + str2 + "/" + str3);
		for(var idx=0; idx<str2.length; idx++) {
			retStr += "*";
		}

		retStr = str1 + "-" + retStr + "-" + str3;
		//alert(retStr);

		return retStr;
	}

	/**
	 * =====================================================
	 * 일반전화 마스킹
	 * =====================================================
	 */
	function maskPhone(mobile) {

		// '-' 구분자 제거
		mobile = mobile.split("-").join("").split(" ").join("");

		if(mobile==null || mobile.length==0 )
			return "";

		// @가 없으면 그냥 리턴
		if(mobile.length < 9)
			return mobile;

		var retStr = "";
		var str1 = mobile.substring(0,2)=="02" ? mobile.substring(0,2) : mobile.substring(0, 3);
		var str2 = mobile.substring((mobile.substring(0,2)=="02" ? 2 : 3), (mobile.length-4));
		var str3 = mobile.substring(mobile.length-4, mobile.length);

		//alert(str1 + "/" + str2 + "/" + str3);
		for(var idx=0; idx<str2.length; idx++) {
			retStr += "*";
		}

		retStr = str1 + "-" + retStr + "-" + str3;
		//alert(retStr);

		return retStr;
	}

	/**
	 * =====================================================
	 * 핸드폰 split
	 * =====================================================
	 */
	function splitMobile(mobile) {

		mobile = mobile.split("-").join("").split(" ").join("");

		if(mobile==null || mobile.length==0 )
			return "";

		if(mobile.length < 10)
			return mobile;

		var retStr = "";
		var str1 = mobile.substring(0, 3);
		var str2 = mobile.substring(3, (mobile.length-4));
		var str3 = mobile.substring(mobile.length-4, mobile.length);

		return str1 + "-" + str2 + "-" + str3;
	}

	/**
	 * =====================================================
	 * 공백이 입력되었는지 검사
	 * =====================================================
	 */
	function checkSpace( str ) {
		if(str.search(/\s/) != -1){
			return true;
		} else {
			return false;
		}
	}

	function onlyNumberInput(obj)
	{
		var str = obj.value;
		str = new String(str);
		var rex = /[^0-9]/g;
		str=str.replace(rex,'');
		obj.value = str;
	}


	/**
	 * =====================================================
	 * Added by CWYOO at 2014.09.02
	 * 만 14세 미만 확인(생년월일로 비교)
	 * =====================================================
	 */
	function calculateAge2(birthDt){
		var rcode = -1;
		var sql = "SPOCLUB.GET.SERVER.DATE";
		var param = new Array();
		rcode = ajaxobj.HR_SELECTINTO(dbname, sql, param, true);

		if(rcode<0){
			alert(ajaxobj.errmsg);
			return;
		}

		var now = ajaxobj.results[0][0];

		var todayYear = Number(now.substr(0,4));
		var todayMonth = Number(now.substr(4,2));
		var todayDay = Number(now.substr(6,2));

		var ssnYear = Number(birthDt.substr(0,4));
		var ssnMonth = Number(birthDt.substr(4,2));
		var ssnDay = Number(birthDt.substr(6,2));

		var manAge = todayYear - ssnYear;

		if(todayMonth < ssnMonth){
			manAge = manAge -1;
		}else if(todayMonth == ssnMonth){
			if(todayDay < ssnDay){
				manAge = manAge -1;
			}
		}
		return manAge;
	}

	/**
	 * =====================================================
	 * 형식검사 관련 함수
	 * =====================================================
	 */
	// 0 ~ 9
	/*
	function CheckNumber(){
		//alert(event.keyCode);
		//if ((event.keyCode>=48 && event.keyCode<=57)) { event.returnValue=true;  }
		if ((event.keyCode>=48 && event.keyCode<=57) || event.keyCode==8 || event.keyCode==46 || event.keyCode==37 || event.keyCode==39 || event.keyCode==9) { event.returnValue=true;  }
		else  { event.returnValue=false;  }
	}
	*/
	// 0 ~ 9
	function CheckNumber(){
		/*
		event.preventDefault();
		if ((event.keyCode>=48 && event.keyCode<=57)) { event.returnValue=true;  }
		else  { event.returnValue=false;  }
		*/
		//alert(event.keyCode);
		if((event.keyCode>=48 && event.keyCode<=57)|| (96<=event.keyCode && event.keyCode<=105) || (event.keyCode==9) || (event.keyCode==8) || (event.keyCode==46)) {
			return;
		}
		event.preventDefault();
	}

	// 0 ~ 9,"-"(45)
	function CheckNumberBar(){
		console.log(event.keyCode);
		if ((48<=event.keyCode && event.keyCode<=57) || (96<=event.keyCode && event.keyCode<=105) || (event.keyCode==8)||(event.keyCode==9) ||(event.keyCode==109)|| (event.keyCode==189)) {
			return;
			}
		event.preventDefault();
	}

	// 0 ~ 9,"."(46)
	function CheckNumberDot(){
		if ((48<=event.keyCode && event.keyCode<=57) || (event.keyCode==46)) { event.returnValue=true;  }
		else  { event.returnValue=false;  }
	}

	// 0 ~ 9,"."(46),"-"(45)
	function CheckNumberBarDot(){
		if ((48<=event.keyCode && event.keyCode<=57) || (event.keyCode==45) || (event.keyCode==46)) { event.returnValue=true;  }
		else  { event.returnValue=false;  }
	}

	// 0 ~ 9,"-"," "(32),":"(58),"/"(47)
	function CheckNumberDateTime(){
		if ((48<=event.keyCode && event.keyCode<=58) || (event.keyCode==45) || (event.keyCode==47) || (event.keyCode==32)) { event.returnValue=true;  }
		else  { event.returnValue=false;  }
	}

	// 0 ~ 9,"-", "."(46)
	function CheckMoney(){
		if ((48<=event.keyCode && event.keyCode<=57) || (event.keyCode==45) || (event.keyCode==46)) { event.returnValue=true;  }
		else  { event.returnValue=false;  }
	}

	// A~Z, " "(SPACE)
	function CheckCapital(){
		if ((65<=event.keyCode && event.keyCode<=90) || (event.keyCode==32)) { event.returnValue=true;  }
		else  { event.returnValue=false;  }
	}

	// A~Z, a~z, " "(SPACE)
	function CheckAlphabet(){
		if ((65<=event.keyCode && event.keyCode<=90) || (97<=event.keyCode && event.keyCode<=122) || (event.keyCode==32)) { event.returnValue=true;  }
		else  { event.returnValue=false;  }
	}



/*****************************************************
               HTML 관련 함수
*****************************************************/
  // 설  명 : 입력상자의 값에 해당하는 선택박스의 인덱스를 설정한다.
  // 작성자 : 이상용
  function set_select ( txt_ele, sel_ele )
  {
      ok_flag = 0;
      txt_value = txt_ele.value.toUpperCase();
      if (txt_value == "") {  sel_ele.options[0].selected = true;  ok_flag = 1;  }
      else
      {
          for(var i = 0; i < sel_ele.length; i++)
          {
              if(txt_value == sel_ele.options[i].value)
              {
                  sel_ele.options[i].selected = true;
                  ok_flag = 1;
              }
          }
      }
      if (ok_flag == 0)
      {
          if (MESSAGE_FG=="ENG") {
              alert("[" + txt_value +"] is not Found.");
          }else{
              alert("[" + txt_value +"]코드는 존재하지 않습니다. 확인후 다시 선택하세요.");
          }
          txt_ele.value = '';
          sel_ele.options[0].selected = true;
          txt_ele.focus();
          return false;
      }
      return true;
  }
  
	/**
	 * =====================================================
	 * 필수입력항목 체크
	 * =====================================================
	 */
	function requiredField(obj,errMsg){
		if (trim(obj.value) == ""){
			alert(errMsg);
			obj.focus();
			return false;
		}
		return true;
	}

	/**
	 * =====================================================
	 * 앞/뒤에서 White Space가 제거된 값반환
	 * =====================================================
	 */
	function trim(value)  {
  		return value.replace(/^\s+|\s+$/g,"");
	}


	/**
	 * =====================================================
	 * RADIO BUTTON Checked value get : set  ....
	 * =====================================================
	 */
	function getRadioCheckedValue(radioObj) {
		if(!radioObj)
			return "";
		var radioLength = radioObj.length;
		if(radioLength == undefined)
			if(radioObj.checked)
				return radioObj.value;
			else
				return "";
		for(var i = 0; i < radioLength; i++) {
			if(radioObj[i].checked) {
				return radioObj[i].value;
			}
		}
		return "";
	}

	function setRadioCheckedValue(radioObj, newValue) {
		if(!radioObj)
			return;
		var radioLength = radioObj.length;
		if(radioLength == undefined) {
			radioObj.checked = (radioObj.value == newValue.toString());
			return;
		}
		for(var i = 0; i < radioLength; i++) {
			radioObj[i].checked = false;
			if(radioObj[i].value == newValue.toString()) {
				radioObj[i].checked = true;
			}
		}
	}
	
	// Added by CWYOO at 2016.11.09
  function convnullspace(obj) {
    var result = new Object();
    for (var i in obj) {
      if (obj.hasOwnProperty(i)) {
          if ( obj[i] == null ) {
            result[i] = "";
          }
          else {
            result[i] = obj[i];
          }
          if($.isArray( result[i])) {
              result[i] = convArraynullspace(obj[i]);
          }
      }
    }
    return result;
  }
  
  // Added by CWYOO at 2016.11.09
  function convArraynullspace(arr) {
    var retobj = new Object();
    var retarr = new Array();
    for (var j=0;j<arr.length;j++) {
      retobj = convnullspace(arr[j]);
      retarr.push(retobj);
    }
    return retarr;
  }
  
  // Added by CWYOO at 2016.11.09
  function isArray(s) {
    return s.constructor.toString().indexOf("Array") > -1; //  배열이면 true  배열이 아니면  false값을 반환
  }

  /**
   * Added by CWYOO at 2017.12.18
   */
  function resizeImg(imgId) {
    //alert(imgId);
    var obj = findObject(imgId);
	if(isValidObj(obj)) {
      if(obj.width > 800) {
        obj.width = 800;
      } else {
        //alert(obj.width);
      }
    }
  }

  function replaceNull(val) {
  	if(val==undefined || val==null || val=="undefined" || val=="null")
  		return "";
  	else
  		return val;
  }
  function replaceNullDelim(val, delim) {
  	if(val==undefined || val==null || val=="undefined" || val=="null" || val=="")
  		return delim;
  	else
  		return val;
  }
