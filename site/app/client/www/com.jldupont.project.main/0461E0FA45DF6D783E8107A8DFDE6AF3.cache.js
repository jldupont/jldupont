(function(){var $wnd = window;var $doc = $wnd.document;var $moduleName, $moduleBase;var _,iu='com.google.gwt.core.client.',ju='com.google.gwt.lang.',ku='com.google.gwt.user.client.',lu='com.google.gwt.user.client.impl.',mu='com.google.gwt.user.client.ui.',nu='com.google.gwt.user.client.ui.impl.',ou='com.jldupont.project.client.',pu='java.lang.',qu='java.util.';function hu(){}
function Bo(a){return this===a;}
function Co(){return mp(this);}
function zo(){}
_=zo.prototype={};_.eQ=Bo;_.hC=Co;_.tI=1;var o=null;function r(a){return a==null?0:a.$H?a.$H:(a.$H=t());}
function s(a){return a==null?0:a.$H?a.$H:(a.$H=t());}
function t(){return ++u;}
var u=0;function x(b,a){if(!lb(a,2)){return false;}return B(b,kb(a,2));}
function y(a){return r(a);}
function z(){return [];}
function A(){return {};}
function C(a){return x(this,a);}
function B(a,b){return a===b;}
function D(){return y(this);}
function v(){}
_=v.prototype=new zo();_.eQ=C;_.hC=D;_.tI=7;function F(c,a,d,b,e){c.a=a;c.b=b;e;c.tI=d;return c;}
function bb(a,b,c){return a[b]=c;}
function cb(b,a){return b[a];}
function db(a){return a.length;}
function fb(e,d,c,b,a){return eb(e,d,c,b,0,db(b),a);}
function eb(j,i,g,c,e,a,b){var d,f,h;if((f=cb(c,e))<0){throw new qo();}h=F(new E(),f,cb(i,e),cb(g,e),j);++e;if(e<a){j=dp(j,1);for(d=0;d<f;++d){bb(h,d,eb(j,i,g,c,e,a,b));}}else{for(d=0;d<f;++d){bb(h,d,b);}}return h;}
function gb(a,b,c){if(c!==null&&a.b!=0&& !lb(c,a.b)){throw new vn();}return bb(a,b,c);}
function E(){}
_=E.prototype=new zo();_.tI=0;function jb(b,a){return !(!(b&&pb[b][a]));}
function kb(b,a){if(b!=null)jb(b.tI,a)||ob();return b;}
function lb(b,a){return b!=null&&jb(b.tI,a);}
function mb(a){if(a>(ko(),lo))return ko(),lo;if(a<(ko(),mo))return ko(),mo;return a>=0?Math.floor(a):Math.ceil(a);}
function ob(){throw new yn();}
function nb(a){if(a!==null){throw new yn();}return a;}
function qb(b,d){_=d.prototype;if(b&& !(b.tI>=_.tI)){var c=b.toString;for(var a in _){b[a]=_[a];}b.toString=c;}return b;}
var pb;function op(b,a){a;return b;}
function np(){}
_=np.prototype=new zo();_.tI=3;function Dn(b,a){op(b,a);return b;}
function Cn(){}
_=Cn.prototype=new np();_.tI=4;function Eo(b,a){Dn(b,a);return b;}
function Do(){}
_=Do.prototype=new Cn();_.tI=5;function ub(b,a){return b;}
function tb(){}
_=tb.prototype=new Do();_.tI=8;function kc(a){a.a=yb(new xb(),a);a.b=xr(new vr());a.d=Cb(new Bb(),a);a.f=ac(new Fb(),a);}
function lc(a){kc(a);return a;}
function nc(c){var a,b,d;a=cc(c.f);fc(c.f);b=null;if(lb(a,4)){b=ub(new tb(),kb(a,4));}else{}if(b!==null){d=o;}qc(c,false);pc(c);}
function oc(e,d){var a,b,c,f;f=false;try{qc(e,true);gc(e.f,e.b.b);te(e.a,10000);while(dc(e.f)){b=ec(e.f);c=true;try{if(b===null){return;}if(lb(b,4)){a=kb(b,4);a.p();}else{}}finally{f=hc(e.f);if(f){return;}if(c){fc(e.f);}}if(tc(lp(),d)){return;}}}finally{if(!f){qe(e.a);qc(e,false);pc(e);}}}
function pc(a){if(!Er(a.b)&& !a.e&& !a.c){rc(a,true);te(a.d,1);}}
function qc(b,a){b.c=a;}
function rc(b,a){b.e=a;}
function sc(b,a){yr(b.b,a);pc(b);}
function tc(a,b){return po(a-b)>=100;}
function wb(){}
_=wb.prototype=new zo();_.tI=0;_.c=false;_.e=false;function re(){re=hu;ze=xr(new vr());{ye();}}
function pe(a){re();return a;}
function qe(a){if(a.b){ue(a.c);}else{ve(a.c);}as(ze,a);}
function se(a){if(!a.b){as(ze,a);}a.bb();}
function te(b,a){if(a<=0){throw ao(new Fn(),'must be positive');}qe(b);b.b=false;b.c=we(b,a);yr(ze,b);}
function ue(a){re();$wnd.clearInterval(a);}
function ve(a){re();$wnd.clearTimeout(a);}
function we(b,a){re();return $wnd.setTimeout(function(){b.q();},a);}
function xe(){var a;a=o;{se(this);}}
function ye(){re();Ee(new le());}
function ke(){}
_=ke.prototype=new zo();_.q=xe;_.tI=9;_.b=false;_.c=0;var ze;function zb(){zb=hu;re();}
function yb(b,a){zb();b.a=a;pe(b);return b;}
function Ab(){if(!this.a.c){return;}nc(this.a);}
function xb(){}
_=xb.prototype=new ke();_.bb=Ab;_.tI=10;function Db(){Db=hu;re();}
function Cb(b,a){Db();b.a=a;pe(b);return b;}
function Eb(){rc(this.a,false);oc(this.a,lp());}
function Bb(){}
_=Bb.prototype=new ke();_.bb=Eb;_.tI=11;function ac(b,a){b.d=a;return b;}
function cc(a){return Br(a.d.b,a.b);}
function dc(a){return a.c<a.a;}
function ec(b){var a;b.b=b.c;a=Br(b.d.b,b.c++);if(b.c>=b.a){b.c=0;}return a;}
function fc(a){Fr(a.d.b,a.b);--a.a;if(a.b<=a.c){if(--a.c<0){a.c=0;}}a.b=(-1);}
function gc(b,a){b.a=a;}
function hc(a){return a.b==(-1);}
function ic(){return dc(this);}
function jc(){return ec(this);}
function Fb(){}
_=Fb.prototype=new zo();_.v=ic;_.y=jc;_.tI=0;_.a=0;_.b=(-1);_.c=0;function wc(){wc=hu;sd=xr(new vr());{md=new nf();yf(md);}}
function xc(b,a){wc();Bf(md,b,a);}
function yc(a,b){wc();return tf(md,a,b);}
function zc(){wc();return Df(md,'A');}
function Ac(){wc();return Df(md,'div');}
function Bc(a){wc();return Df(md,a);}
function Cc(){wc();return Df(md,'img');}
function Dc(){wc();return Ef(md,'text');}
function Ec(){wc();return Df(md,'tbody');}
function Fc(){wc();return Df(md,'tr');}
function ad(){wc();return Df(md,'table');}
function dd(b,a,d){wc();var c;c=o;{cd(b,a,d);}}
function cd(b,a,c){wc();var d;if(a===rd){if(fd(b)==8192){rd=null;}}d=bd;bd=b;try{c.z(b);}finally{bd=d;}}
function ed(b,a){wc();Ff(md,b,a);}
function fd(a){wc();return ag(md,a);}
function gd(a){wc();uf(md,a);}
function hd(b,a){wc();return vf(md,b,a);}
function id(a,b){wc();return bg(md,a,b);}
function jd(a){wc();return cg(md,a);}
function kd(a){wc();return wf(md,a);}
function ld(a){wc();return xf(md,a);}
function nd(c,a,b){wc();zf(md,c,a,b);}
function od(a){wc();var b,c;c=true;if(sd.b>0){b=nb(Br(sd,sd.b-1));if(!(c=null.fb())){ed(a,true);gd(a);}}return c;}
function pd(b,a){wc();dg(md,b,a);}
function qd(b,a){wc();eg(md,b,a);}
function td(b,a,c){wc();fg(md,b,a,c);}
function vd(a,b,c){wc();hg(md,a,b,c);}
function ud(a,b,c){wc();gg(md,a,b,c);}
function wd(a,b){wc();ig(md,a,b);}
function xd(a,b){wc();jg(md,a,b);}
function yd(a,b){wc();kg(md,a,b);}
function zd(b,a,c){wc();lg(md,b,a,c);}
function Ad(a,b){wc();Af(md,a,b);}
function Bd(){wc();return pf(md);}
function Cd(){wc();return qf(md);}
var bd=null,md=null,rd=null,sd;function Ed(){Ed=hu;ae=lc(new wb());}
function Fd(a){Ed();if(a===null){throw to(new so(),'cmd can not be null');}sc(ae,a);}
var ae;function de(a){if(lb(a,5)){return yc(this,kb(a,5));}return x(qb(this,be),a);}
function ee(){return y(qb(this,be));}
function be(){}
_=be.prototype=new v();_.eQ=de;_.hC=ee;_.tI=12;function ie(a){return x(qb(this,fe),a);}
function je(){return y(qb(this,fe));}
function fe(){}
_=fe.prototype=new v();_.eQ=ie;_.hC=je;_.tI=13;function ne(){while((re(),ze).b>0){qe(kb(Br((re(),ze),0),6));}}
function oe(){return null;}
function le(){}
_=le.prototype=new zo();_.C=ne;_.D=oe;_.tI=14;function De(){De=hu;af=xr(new vr());lf=xr(new vr());{gf();}}
function Ee(a){De();yr(af,a);}
function Fe(a){De();yr(lf,a);}
function bf(){De();var a,b;for(a=dq(af);Cp(a);){b=kb(Dp(a),7);b.C();}}
function cf(){De();var a,b,c,d;d=null;for(a=dq(af);Cp(a);){b=kb(Dp(a),7);c=b.D();{d=c;}}return d;}
function df(){De();var a,b;for(a=dq(lf);Cp(a);){b=kb(Dp(a),8);b.E(ff(),ef());}}
function ef(){De();return Bd();}
function ff(){De();return Cd();}
function gf(){De();__gwt_initHandlers(function(){kf();},function(){return jf();},function(){hf();$wnd.onresize=null;$wnd.onbeforeclose=null;$wnd.onclose=null;});}
function hf(){De();var a;a=o;{bf();}}
function jf(){De();var a;a=o;{return cf();}}
function kf(){De();var a;a=o;{df();}}
var af,lf;function Bf(c,b,a){b.appendChild(a);}
function Df(b,a){return $doc.createElement(a);}
function Ef(b,c){var a=$doc.createElement('INPUT');a.type=c;return a;}
function Ff(c,b,a){b.cancelBubble=a;}
function ag(b,a){switch(a.type){case 'blur':return 4096;case 'change':return 1024;case 'click':return 1;case 'dblclick':return 2;case 'focus':return 2048;case 'keydown':return 128;case 'keypress':return 256;case 'keyup':return 512;case 'load':return 32768;case 'losecapture':return 8192;case 'mousedown':return 4;case 'mousemove':return 64;case 'mouseout':return 32;case 'mouseover':return 16;case 'mouseup':return 8;case 'scroll':return 16384;case 'error':return 65536;case 'mousewheel':return 131072;case 'DOMMouseScroll':return 131072;}}
function bg(d,a,c){var b=parseInt(a[c]);if(!b){return 0;}return b;}
function cg(b,a){return a.__eventBits||0;}
function dg(c,b,a){b.removeChild(a);}
function eg(c,b,a){b.removeAttribute(a);}
function fg(c,b,a,d){b.setAttribute(a,d);}
function hg(c,a,b,d){a[b]=d;}
function gg(c,a,b,d){a[b]=d;}
function ig(c,a,b){a.__listener=b;}
function jg(c,a,b){a.src=b;}
function kg(c,a,b){if(!b){b='';}a.innerHTML=b;}
function lg(c,b,a,d){b.style[a]=d;}
function mf(){}
_=mf.prototype=new zo();_.tI=0;function tf(c,a,b){return a==b;}
function uf(b,a){a.preventDefault();}
function vf(f,c,d){var b=0,a=c.firstChild;while(a){var e=a.nextSibling;if(a.nodeType==1){if(d==b)return a;++b;}a=e;}return null;}
function wf(c,b){var a=b.firstChild;while(a&&a.nodeType!=1)a=a.nextSibling;return a||null;}
function xf(c,a){var b=a.parentNode;if(b==null){return null;}if(b.nodeType!=1)b=null;return b||null;}
function yf(d){$wnd.__dispatchCapturedMouseEvent=function(b){if($wnd.__dispatchCapturedEvent(b)){var a=$wnd.__captureElem;if(a&&a.__listener){dd(b,a,a.__listener);b.stopPropagation();}}};$wnd.__dispatchCapturedEvent=function(a){if(!od(a)){a.stopPropagation();a.preventDefault();return false;}return true;};$wnd.addEventListener('click',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('dblclick',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousedown',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mouseup',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousemove',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousewheel',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('keydown',$wnd.__dispatchCapturedEvent,true);$wnd.addEventListener('keyup',$wnd.__dispatchCapturedEvent,true);$wnd.addEventListener('keypress',$wnd.__dispatchCapturedEvent,true);$wnd.__dispatchEvent=function(b){var c,a=this;while(a&& !(c=a.__listener))a=a.parentNode;if(a&&a.nodeType!=1)a=null;if(c)dd(b,a,c);};$wnd.__captureElem=null;}
function zf(f,e,g,d){var c=0,b=e.firstChild,a=null;while(b){if(b.nodeType==1){if(c==d){a=b;break;}++c;}b=b.nextSibling;}e.insertBefore(g,a);}
function Af(c,b,a){b.__eventBits=a;b.onclick=a&1?$wnd.__dispatchEvent:null;b.ondblclick=a&2?$wnd.__dispatchEvent:null;b.onmousedown=a&4?$wnd.__dispatchEvent:null;b.onmouseup=a&8?$wnd.__dispatchEvent:null;b.onmouseover=a&16?$wnd.__dispatchEvent:null;b.onmouseout=a&32?$wnd.__dispatchEvent:null;b.onmousemove=a&64?$wnd.__dispatchEvent:null;b.onkeydown=a&128?$wnd.__dispatchEvent:null;b.onkeypress=a&256?$wnd.__dispatchEvent:null;b.onkeyup=a&512?$wnd.__dispatchEvent:null;b.onchange=a&1024?$wnd.__dispatchEvent:null;b.onfocus=a&2048?$wnd.__dispatchEvent:null;b.onblur=a&4096?$wnd.__dispatchEvent:null;b.onlosecapture=a&8192?$wnd.__dispatchEvent:null;b.onscroll=a&16384?$wnd.__dispatchEvent:null;b.onload=a&32768?$wnd.__dispatchEvent:null;b.onerror=a&65536?$wnd.__dispatchEvent:null;b.onmousewheel=a&131072?$wnd.__dispatchEvent:null;}
function rf(){}
_=rf.prototype=new mf();_.tI=0;function pf(a){return $wnd.innerHeight;}
function qf(a){return $wnd.innerWidth;}
function nf(){}
_=nf.prototype=new rf();_.tI=0;function kl(a){return id(a.h,'offsetWidth');}
function ll(d,b,a){var c=b.parentNode;if(!c){return;}c.insertBefore(a,b);c.removeChild(b);}
function ml(b,a){if(b.h!==null){ll(b,b.h,a);}b.h=a;}
function nl(b,a){zd(b.h,'height',a);}
function ol(b,c,a){sl(b,c);nl(b,a);}
function pl(b,a){ul(b.h,a);}
function ql(b,a){vl(b.h,a);}
function rl(a,b){if(b===null||cp(b)==0){qd(a.h,'title');}else{td(a.h,'title',b);}}
function sl(a,b){zd(a.h,'width',b);}
function tl(b,a){Ad(b.h,a|jd(b.h));}
function ul(a,b){vd(a,'className',b);}
function vl(a,b){if(a===null){throw Eo(new Do(),'Null widget handle. If you are creating a composite, ensure that initWidget() has been called.');}b=ep(b);if(cp(b)==0){throw ao(new Fn(),'Style names cannot be empty');}wl(a,b);}
function wl(b,f){var a=b.className.split(/\s+/);if(!a){return;}var g=a[0];var h=g.length;a[0]=f;for(var c=1,d=a.length;c<d;c++){var e=a[c];if(e.length>h&&(e.charAt(h)=='-'&&e.indexOf(g)==0)){a[c]=f+e.substring(h);}}b.className=a.join(' ');}
function il(){}
_=il.prototype=new zo();_.tI=0;_.h=null;function hm(a){if(a.f){throw eo(new co(),"Should only call onAttach when the widget is detached from the browser's document");}a.f=true;wd(a.h,a);a.m();a.A();}
function im(a){if(!a.f){throw eo(new co(),"Should only call onDetach when the widget is attached to the browser's document");}try{a.B();}finally{a.n();wd(a.h,null);a.f=false;}}
function jm(a){if(a.g!==null){a.g.ab(a);}else if(a.g!==null){throw eo(new co(),"This widget's parent does not implement HasWidgets");}}
function km(b,a){if(b.f){wd(b.h,null);}ml(b,a);if(b.f){wd(a,b);}}
function lm(c,b){var a;a=c.g;if(b===null){if(a!==null&&a.f){im(c);}c.g=null;}else{if(a!==null){throw eo(new co(),'Cannot set a new parent without first clearing the old parent');}c.g=b;if(b.f){hm(c);}}}
function mm(){}
function nm(){}
function om(a){}
function pm(){}
function qm(){}
function rm(a){km(this,a);}
function xl(){}
_=xl.prototype=new il();_.m=mm;_.n=nm;_.z=om;_.A=pm;_.B=qm;_.cb=rm;_.tI=15;_.f=false;_.g=null;function ak(b,a){lm(a,b);}
function ck(b,a){lm(a,null);}
function dk(){var a,b;for(b=this.w();b.v();){a=kb(b.y(),9);hm(a);}}
function ek(){var a,b;for(b=this.w();b.v();){a=kb(b.y(),9);im(a);}}
function fk(){}
function gk(){}
function Fj(){}
_=Fj.prototype=new xl();_.m=dk;_.n=ek;_.A=fk;_.B=gk;_.tI=16;function vg(a){a.a=El(new yl(),a);}
function wg(a){vg(a);return a;}
function xg(c,a,b){jm(a);Fl(c.a,a);xc(b,a.h);ak(c,a);}
function zg(b,c){var a;if(c.g!==b){return false;}ck(b,c);a=c.h;pd(ld(a),a);fm(b.a,c);return true;}
function Ag(){return dm(this.a);}
function Bg(a){return zg(this,a);}
function ug(){}
_=ug.prototype=new Fj();_.w=Ag;_.ab=Bg;_.tI=17;function ng(a){wg(a);a.cb(Ac());zd(a.h,'position','relative');zd(a.h,'overflow','hidden');return a;}
function og(a,b){xg(a,b,a.h);}
function pg(b,d,a,c){jm(d);rg(b,d,a,c);og(b,d);}
function rg(c,e,b,d){var a;a=e.h;if(b==(-1)&&d==(-1)){sg(a);}else{zd(a,'position','absolute');zd(a,'left',b+'px');zd(a,'top',d+'px');}}
function sg(a){zd(a,'left','');zd(a,'top','');zd(a,'position','');}
function tg(b){var a;a=zg(this,b);if(a){sg(b.h);}return a;}
function mg(){}
_=mg.prototype=new ug();_.ab=tg;_.tI=18;function ui(a){a.e=ki(new fi());}
function vi(a){ui(a);a.d=ad();a.a=Ec();xc(a.d,a.a);a.cb(a.d);tl(a,1);return a;}
function wi(c,a){var b;b=eh(c);if(a>=b||a<0){throw ho(new go(),'Row index: '+a+', Row size: '+b);}}
function xi(e,c,b,a){var d;d=Eh(e.b,c,b);Di(e,d,a);return d;}
function zi(c,b,a){return b.rows[a].cells.length;}
function Ai(a){return Bi(a,a.a);}
function Bi(b,a){return a.rows.length;}
function Ci(b,a){var c;if(a!=eh(b)){wi(b,a);}c=Fc();nd(b.a,c,a);return a;}
function Di(d,c,a){var b,e;b=kd(c);e=null;if(b!==null){e=mi(d.e,b);}if(e!==null){Ei(d,e);return true;}else{if(a){yd(c,'');}return false;}}
function Ei(b,c){var a;if(c.g!==b){return false;}ck(b,c);a=c.h;pd(ld(a),a);pi(b.e,a);return true;}
function Fi(a,b){vd(a.d,'border',''+b);}
function aj(b,a){b.b=a;}
function bj(b,a){ud(b.d,'cellPadding',a);}
function cj(b,a){ud(b.d,'cellSpacing',a);}
function dj(b,a){b.c=a;ei(b.c);}
function ej(d,b,a,e){var c;gh(d,b,a);if(e!==null){jm(e);c=xi(d,b,a,true);ni(d.e,e);xc(c,e.h);ak(d,e);}}
function fj(){return qi(this.e);}
function gj(a){switch(fd(a)){case 1:{break;}default:}}
function hj(a){return Ei(this,a);}
function qh(){}
_=qh.prototype=new Fj();_.w=fj;_.z=gj;_.ab=hj;_.tI=19;_.a=null;_.b=null;_.c=null;_.d=null;function bh(a){vi(a);aj(a,Eg(new Dg(),a));dj(a,ci(new bi(),a));return a;}
function dh(b,a){wi(b,a);return zi(b,b.a,a);}
function eh(a){return Ai(a);}
function fh(b,a){return Ci(b,a);}
function gh(e,d,b){var a,c;hh(e,d);if(b<0){throw ho(new go(),'Cannot create a column with a negative index: '+b);}a=dh(e,d);c=b+1-a;if(c>0){ih(e.a,d,c);}}
function hh(d,b){var a,c;if(b<0){throw ho(new go(),'Cannot create a row with a negative index: '+b);}c=eh(d);for(a=c;a<=b;a++){fh(d,a);}}
function ih(f,d,c){var e=f.rows[d];for(var b=0;b<c;b++){var a=$doc.createElement('td');e.appendChild(a);}}
function Cg(){}
_=Cg.prototype=new qh();_.tI=20;function Ah(b,a){b.a=a;return b;}
function Ch(c,b,a){gh(c.a,b,a);return Dh(c,c.a.a,b,a);}
function Dh(e,d,c,a){var b=d.rows[c].cells[a];return b==null?null:b;}
function Eh(c,b,a){return Dh(c,c.a.a,b,a);}
function Fh(e,d,b,a){var c;gh(e.a,d,b);c=Dh(e,e.a.a,d,b);vd(c,'align',a.a);}
function ai(c,b,a,d){gh(c.a,b,a);vd(Dh(c,c.a.a,b,a),'width',d);}
function zh(){}
_=zh.prototype=new zo();_.tI=0;function Eg(b,a){Ah(b,a);return b;}
function ah(d,c,b,a){ud(Ch(d,c,b),'colSpan',a);}
function Dg(){}
_=Dg.prototype=new zh();_.tI=0;function lh(){lh=hu;Em(),an;}
function kh(b,a){Em(),an;nh(b,a);return b;}
function mh(b,a){switch(fd(a)){case 1:break;case 4096:case 2048:break;case 128:case 512:case 256:break;}}
function nh(b,a){km(b,a);tl(b,7041);}
function oh(a){mh(this,a);}
function ph(a){nh(this,a);}
function jh(){}
_=jh.prototype=new xl();_.z=oh;_.cb=ph;_.tI=21;function sh(a){{vh(a);}}
function th(b,a){b.b=a;sh(b);return b;}
function vh(a){while(++a.a<a.b.b.b){if(Br(a.b.b,a.a)!==null){return;}}}
function wh(a){return a.a<a.b.b.b;}
function xh(){return wh(this);}
function yh(){var a;if(!wh(this)){throw new du();}a=Br(this.b.b,this.a);vh(this);return a;}
function rh(){}
_=rh.prototype=new zo();_.v=xh;_.y=yh;_.tI=0;_.a=(-1);function ci(b,a){b.b=a;return b;}
function ei(a){if(a.a===null){a.a=Bc('colgroup');nd(a.b.d,a.a,0);xc(a.a,Bc('col'));}}
function bi(){}
_=bi.prototype=new zo();_.tI=0;_.a=null;function ji(a){a.b=xr(new vr());}
function ki(a){ji(a);return a;}
function mi(c,a){var b;b=si(a);if(b<0){return null;}return kb(Br(c.b,b),9);}
function ni(b,c){var a;if(b.a===null){a=b.b.b;yr(b.b,c);}else{a=b.a.a;bs(b.b,a,c);b.a=b.a.b;}ti(c.h,a);}
function oi(c,a,b){ri(a);bs(c.b,b,null);c.a=hi(new gi(),b,c.a);}
function pi(c,a){var b;b=si(a);oi(c,a,b);}
function qi(a){return th(new rh(),a);}
function ri(a){a['__widgetID']=null;}
function si(a){var b=a['__widgetID'];return b==null?-1:b;}
function ti(a,b){a['__widgetID']=b;}
function fi(){}
_=fi.prototype=new zo();_.tI=0;_.a=null;function hi(c,a,b){c.a=a;c.b=b;return c;}
function gi(){}
_=gi.prototype=new zo();_.tI=0;_.a=0;_.b=null;function nj(){nj=hu;oj=lj(new kj(),'center');lj(new kj(),'left');lj(new kj(),'right');}
var oj;function lj(b,a){b.a=a;return b;}
function kj(){}
_=kj.prototype=new zo();_.tI=0;_.a=null;function Bj(){Bj=hu;it(new ps());}
function zj(a){Bj();Aj(a,wj(new vj(),a));pl(a,'gwt-Image');return a;}
function Aj(b,a){b.a=a;}
function Cj(a,b){yj(a.a,a,b);}
function Dj(a){switch(fd(a)){case 1:{break;}case 4:case 8:case 64:case 16:case 32:{break;}case 131072:break;case 32768:{break;}case 65536:{break;}}}
function sj(){}
_=sj.prototype=new xl();_.z=Dj;_.tI=22;_.a=null;function tj(){}
_=tj.prototype=new zo();_.tI=0;function wj(b,a){a.cb(Cc());tl(a,229501);return b;}
function yj(b,a,c){xd(a.h,c);}
function vj(){}
_=vj.prototype=new tj();_.tI=0;function nk(){nk=hu;sk=it(new ps());}
function mk(b,a){nk();ng(b);if(a===null){a=ok();}b.cb(a);hm(b);return b;}
function pk(){nk();return qk(null);}
function qk(c){nk();var a,b;b=kb(ot(sk,c),10);if(b!==null){return b;}a=null;if(sk.c==0){rk();}pt(sk,c,b=mk(new hk(),a));return b;}
function ok(){nk();return $doc.body;}
function rk(){nk();Ee(new ik());}
function hk(){}
_=hk.prototype=new mg();_.tI=23;var sk;function kk(){var a,b;for(b=Cq(kr((nk(),sk)));dr(b);){a=kb(er(b),10);if(a.f){im(a);}}}
function lk(){return null;}
function ik(){}
_=ik.prototype=new zo();_.C=kk;_.D=lk;_.tI=24;function bl(){bl=hu;Em(),an;el=Ek(new Dk(),'center');Ek(new Dk(),'justify');Ek(new Dk(),'left');Ek(new Dk(),'right');}
function al(b,a){bl();kh(b,a);tl(b,1024);return b;}
function dl(b,a){vd(b.h,'value',a!==null?a:'');}
function cl(b,a){zd(b.h,'textAlign',a.a);}
function fl(a){var b;mh(this,a);b=fd(a);}
function Ck(){}
_=Ck.prototype=new jh();_.z=fl;_.tI=25;var el;function hl(){hl=hu;bl();}
function gl(a){hl();al(a,Dc());pl(a,'gwt-TextBox');return a;}
function Bk(){}
_=Bk.prototype=new Ck();_.tI=26;function Ek(b,a){b.a=a;return b;}
function Dk(){}
_=Dk.prototype=new zo();_.tI=0;_.a=null;function El(b,a){b.a=fb('[Lcom.google.gwt.user.client.ui.Widget;',[0],[9],[4],null);return b;}
function Fl(a,b){cm(a,b,a.b);}
function bm(b,c){var a;for(a=0;a<b.b;++a){if(b.a[a]===c){return a;}}return (-1);}
function cm(d,e,a){var b,c;if(a<0||a>d.b){throw new go();}if(d.b==d.a.a){c=fb('[Lcom.google.gwt.user.client.ui.Widget;',[0],[9],[d.a.a*2],null);for(b=0;b<d.a.a;++b){gb(c,b,d.a[b]);}d.a=c;}++d.b;for(b=d.b-1;b>a;--b){gb(d.a,b,d.a[b-1]);}gb(d.a,a,e);}
function dm(a){return Al(new zl(),a);}
function em(c,b){var a;if(b<0||b>=c.b){throw new go();}--c.b;for(a=b;a<c.b;++a){gb(c.a,a,c.a[a+1]);}gb(c.a,c.b,null);}
function fm(b,c){var a;a=bm(b,c);if(a==(-1)){throw new du();}em(b,a);}
function yl(){}
_=yl.prototype=new zo();_.tI=0;_.a=null;_.b=0;function Al(b,a){b.b=a;return b;}
function Cl(){return this.a<this.b.b-1;}
function Dl(){if(this.a>=this.b.b){throw new du();}return this.b.a[++this.a];}
function zl(){}
_=zl.prototype=new zo();_.v=Cl;_.y=Dl;_.tI=0;_.a=(-1);function Em(){Em=hu;Fm=Am(new zm());an=Fm!==null?Dm(new sm()):Fm;}
function Dm(a){Em();return a;}
function sm(){}
_=sm.prototype=new zo();_.tI=0;var Fm,an;function wm(){wm=hu;Em();}
function um(a){xm(a);ym(a);Cm(a);}
function vm(a){wm();Dm(a);um(a);return a;}
function xm(b){return function(a){if(this.parentNode.onblur){this.parentNode.onblur(a);}};}
function ym(b){return function(a){if(this.parentNode.onfocus){this.parentNode.onfocus(a);}};}
function tm(){}
_=tm.prototype=new sm();_.tI=0;function Bm(){Bm=hu;wm();}
function Am(a){Bm();vm(a);return a;}
function Cm(b){return function(){var a=this.firstChild;$wnd.setTimeout(function(){a.focus();},0);};}
function zm(){}
_=zm.prototype=new tm();_.tI=0;function cn(a){a.cb(zc());return a;}
function en(b,a){td(b.h,'href',a===null?'':a);}
function fn(b,a){td(b.h,'id',a===null?'':a);}
function gn(c,d){var a,b;a=c.h;b=hd(a,0);if(b===null){b=Cc();nd(a,b,0);}xd(b,d);}
function hn(b,a){td(b.h,'target',a===null?'':a);}
function bn(){}
_=bn.prototype=new xl();_.tI=27;function on(a){a.f=bh(new Cg());a.b=cn(new bn());a.a=cn(new bn());a.d=cn(new bn());a.c=cn(new bn());a.e=gl(new Bk());}
function qn(a){on(a);return a;}
function rn(e){var a,b,c,d;pk();d=pk();ol(d,'100%','100%');ql(d,'rootPanel');pl(d,'rootPanel');pg(d,e.f,60,0);Fi(e.f,2);ol(e.f,'377px','270px');cj(e.f,5);bj(e.f,5);ej(e.f,1,0,e.b);Fh(e.f.b,1,0,(nj(),oj));hn(e.b,'_blank');en(e.b,'http://www.linkedin.com/in/JeanLouDupont');fn(e.b,'link_linkedin');gn(e.b,'linkedin.gif');ej(e.f,1,1,e.a);Fh(e.f.b,1,1,(nj(),oj));hn(e.a,'_blank');en(e.a,'http://jldupont.blogspot.com');fn(e.a,'link_blog');gn(e.a,'blog.jpg');ej(e.f,2,0,e.d);Fh(e.f.b,2,0,(nj(),oj));hn(e.d,'_blank');en(e.d,'http://wiki.jldupont.com');fn(e.d,'link_wiki');gn(e.d,'wiki.png');ej(e.f,2,1,e.c);Fh(e.f.b,2,1,(nj(),oj));hn(e.c,'_blank');en(e.c,'http://code.google.com/u/JeanLou.Dupont/');fn(e.c,'link_projects');gn(e.c,'projects.jpg');ej(e.f,0,0,e.e);pl(e.e,'title');cl(e.e,(bl(),el));rl(e.e,'title');Fh(e.f.b,0,0,(nj(),oj));dl(e.e,"Jean-Lou Dupont's WEB site");ah(e.f.b,0,0,2);sl(e.e,'100%');c=bh(new Cg());ej(e.f,3,0,c);Fh(e.f.b,3,0,(nj(),oj));ah(e.f.b,3,0,2);b=zj(new sj());ej(c,0,0,b);ai(c.b,0,0,'43px');Cj(b,'gwt.png');a=zj(new sj());ej(c,0,1,a);ai(c.b,0,1,'50px');Cj(a,'gae.png');Fd(mn(new kn(),e));sn(e,ff(),ef());Fe(e);}
function sn(d,e,b){var a,c,f;a=d.f.h;f=kl(d.f);c=mb((e-f)/2);zd(a,'position','absolute');zd(a,'left',c+'px');}
function tn(b,a){sn(this,b,a);}
function jn(){}
_=jn.prototype=new zo();_.E=tn;_.tI=28;function mn(b,a){b.a=a;return b;}
function nn(){sn(this.a,ff(),ef());}
function kn(){}
_=kn.prototype=new zo();_.p=nn;_.tI=29;function vn(){}
_=vn.prototype=new Do();_.tI=30;function yn(){}
_=yn.prototype=new Do();_.tI=31;function ao(b,a){Eo(b,a);return b;}
function Fn(){}
_=Fn.prototype=new Do();_.tI=32;function eo(b,a){Eo(b,a);return b;}
function co(){}
_=co.prototype=new Do();_.tI=33;function ho(b,a){Eo(b,a);return b;}
function go(){}
_=go.prototype=new Do();_.tI=34;function wo(){wo=hu;{yo();}}
function yo(){wo();xo=/^[+-]?\d*\.?\d*(e[+-]?\d+)?$/i;}
var xo=null;function ko(){ko=hu;wo();}
var lo=2147483647,mo=(-2147483648);function po(a){return a<0?-a:a;}
function qo(){}
_=qo.prototype=new Do();_.tI=35;function to(b,a){Eo(b,a);return b;}
function so(){}
_=so.prototype=new Do();_.tI=36;function cp(a){return a.length;}
function dp(b,a){return b.substr(a,b.length-a);}
function ep(c){var a=c.replace(/^(\s*)/,'');var b=a.replace(/\s*$/,'');return b;}
function fp(a,b){return String(a)==b;}
function gp(a){if(!lb(a,1))return false;return fp(this,a);}
function ip(){var a=hp;if(!a){a=hp={};}var e=':'+this;var b=a[e];if(b==null){b=0;var f=this.length;var d=f<64?1:f/32|0;for(var c=0;c<f;c+=d){b<<=1;b+=this.charCodeAt(c);}b|=0;a[e]=b;}return b;}
_=String.prototype;_.eQ=gp;_.hC=ip;_.tI=2;var hp=null;function lp(){return new Date().getTime();}
function mp(a){return s(a);}
function rp(b,a){Eo(b,a);return b;}
function qp(){}
_=qp.prototype=new Do();_.tI=37;function up(d,a,b){var c;while(a.v()){c=a.y();if(b===null?c===null:b.eQ(c)){return a;}}return null;}
function wp(a){throw rp(new qp(),'add');}
function xp(b){var a;a=up(this,this.w(),b);return a!==null;}
function tp(){}
_=tp.prototype=new zo();_.j=wp;_.l=xp;_.tI=0;function cq(b,a){throw ho(new go(),'Index: '+a+', Size: '+b.b);}
function dq(a){return Ap(new zp(),a);}
function eq(b,a){throw rp(new qp(),'add');}
function fq(a){this.i(this.db(),a);return true;}
function gq(e){var a,b,c,d,f;if(e===this){return true;}if(!lb(e,14)){return false;}f=kb(e,14);if(this.db()!=f.db()){return false;}c=dq(this);d=f.w();while(Cp(c)){a=Dp(c);b=Dp(d);if(!(a===null?b===null:a.eQ(b))){return false;}}return true;}
function hq(){var a,b,c,d;c=1;a=31;b=dq(this);while(Cp(b)){d=Dp(b);c=31*c+(d===null?0:d.hC());}return c;}
function iq(){return dq(this);}
function jq(a){throw rp(new qp(),'remove');}
function yp(){}
_=yp.prototype=new tp();_.i=eq;_.j=fq;_.eQ=gq;_.hC=hq;_.w=iq;_.F=jq;_.tI=38;function Ap(b,a){b.c=a;return b;}
function Cp(a){return a.a<a.c.db();}
function Dp(a){if(!Cp(a)){throw new du();}return a.c.t(a.b=a.a++);}
function Ep(a){if(a.b<0){throw new co();}a.c.F(a.b);a.a=a.b;a.b=(-1);}
function Fp(){return Cp(this);}
function aq(){return Dp(this);}
function zp(){}
_=zp.prototype=new zo();_.v=Fp;_.y=aq;_.tI=0;_.a=0;_.b=(-1);function ir(f,d,e){var a,b,c;for(b=dt(f.o());Cs(b);){a=Ds(b);c=a.r();if(d===null?c===null:d.eQ(c)){if(e){Es(b);}return a;}}return null;}
function jr(b){var a;a=b.o();return mq(new lq(),b,a);}
function kr(b){var a;a=nt(b);return Aq(new zq(),b,a);}
function lr(a){return ir(this,a,false)!==null;}
function mr(d){var a,b,c,e,f,g,h;if(d===this){return true;}if(!lb(d,15)){return false;}f=kb(d,15);c=jr(this);e=f.x();if(!sr(c,e)){return false;}for(a=oq(c);vq(a);){b=wq(a);h=this.u(b);g=f.u(b);if(h===null?g!==null:!h.eQ(g)){return false;}}return true;}
function nr(b){var a;a=ir(this,b,false);return a===null?null:a.s();}
function or(){var a,b,c;b=0;for(c=dt(this.o());Cs(c);){a=Ds(c);b+=a.hC();}return b;}
function pr(){return jr(this);}
function kq(){}
_=kq.prototype=new zo();_.k=lr;_.eQ=mr;_.u=nr;_.hC=or;_.x=pr;_.tI=39;function sr(e,b){var a,c,d;if(b===e){return true;}if(!lb(b,16)){return false;}c=kb(b,16);if(c.db()!=e.db()){return false;}for(a=c.w();a.v();){d=a.y();if(!e.l(d)){return false;}}return true;}
function tr(a){return sr(this,a);}
function ur(){var a,b,c;a=0;for(b=this.w();b.v();){c=b.y();if(c!==null){a+=c.hC();}}return a;}
function qr(){}
_=qr.prototype=new tp();_.eQ=tr;_.hC=ur;_.tI=40;function mq(b,a,c){b.a=a;b.b=c;return b;}
function oq(b){var a;a=dt(b.b);return tq(new sq(),b,a);}
function pq(a){return this.a.k(a);}
function qq(){return oq(this);}
function rq(){return this.b.a.c;}
function lq(){}
_=lq.prototype=new qr();_.l=pq;_.w=qq;_.db=rq;_.tI=41;function tq(b,a,c){b.a=c;return b;}
function vq(a){return a.a.v();}
function wq(b){var a;a=b.a.y();return a.r();}
function xq(){return vq(this);}
function yq(){return wq(this);}
function sq(){}
_=sq.prototype=new zo();_.v=xq;_.y=yq;_.tI=0;function Aq(b,a,c){b.a=a;b.b=c;return b;}
function Cq(b){var a;a=dt(b.b);return br(new ar(),b,a);}
function Dq(a){return mt(this.a,a);}
function Eq(){return Cq(this);}
function Fq(){return this.b.a.c;}
function zq(){}
_=zq.prototype=new tp();_.l=Dq;_.w=Eq;_.db=Fq;_.tI=0;function br(b,a,c){b.a=c;return b;}
function dr(a){return a.a.v();}
function er(a){var b;b=a.a.y().s();return b;}
function fr(){return dr(this);}
function gr(){return er(this);}
function ar(){}
_=ar.prototype=new zo();_.v=fr;_.y=gr;_.tI=0;function wr(a){{zr(a);}}
function xr(a){wr(a);return a;}
function yr(b,a){ls(b.a,b.b++,a);return true;}
function zr(a){a.a=z();a.b=0;}
function Br(b,a){if(a<0||a>=b.b){cq(b,a);}return hs(b.a,a);}
function Cr(b,a){return Dr(b,a,0);}
function Dr(c,b,a){if(a<0){cq(c,a);}for(;a<c.b;++a){if(gs(b,hs(c.a,a))){return a;}}return (-1);}
function Er(a){return a.b==0;}
function Fr(c,a){var b;b=Br(c,a);js(c.a,a,1);--c.b;return b;}
function as(c,b){var a;a=Cr(c,b);if(a==(-1)){return false;}Fr(c,a);return true;}
function bs(d,a,b){var c;c=Br(d,a);ls(d.a,a,b);return c;}
function ds(a,b){if(a<0||a>this.b){cq(this,a);}cs(this.a,a,b);++this.b;}
function es(a){return yr(this,a);}
function cs(a,b,c){a.splice(b,0,c);}
function fs(a){return Cr(this,a)!=(-1);}
function gs(a,b){return a===b||a!==null&&a.eQ(b);}
function is(a){return Br(this,a);}
function hs(a,b){return a[b];}
function ks(a){return Fr(this,a);}
function js(a,c,b){a.splice(c,b);}
function ls(a,b,c){a[b]=c;}
function ms(){return this.b;}
function vr(){}
_=vr.prototype=new yp();_.i=ds;_.j=es;_.l=fs;_.t=is;_.F=ks;_.db=ms;_.tI=42;_.a=null;_.b=0;function kt(){kt=hu;rt=xt();}
function ht(a){{jt(a);}}
function it(a){kt();ht(a);return a;}
function jt(a){a.a=z();a.d=A();a.b=qb(rt,v);a.c=0;}
function lt(b,a){if(lb(a,1)){return Bt(b.d,kb(a,1))!==rt;}else if(a===null){return b.b!==rt;}else{return At(b.a,a,a.hC())!==rt;}}
function mt(a,b){if(a.b!==rt&&zt(a.b,b)){return true;}else if(wt(a.d,b)){return true;}else if(ut(a.a,b)){return true;}return false;}
function nt(a){return bt(new ys(),a);}
function ot(c,a){var b;if(lb(a,1)){b=Bt(c.d,kb(a,1));}else if(a===null){b=c.b;}else{b=At(c.a,a,a.hC());}return b===rt?null:b;}
function pt(c,a,d){var b;{b=c.b;c.b=d;}if(b===rt){++c.c;return null;}else{return b;}}
function qt(c,a){var b;if(lb(a,1)){b=Et(c.d,kb(a,1));}else if(a===null){b=c.b;c.b=qb(rt,v);}else{b=Dt(c.a,a,a.hC());}if(b===rt){return null;}else{--c.c;return b;}}
function st(e,c){kt();for(var d in e){if(d==parseInt(d)){var a=e[d];for(var f=0,b=a.length;f<b;++f){c.j(a[f]);}}}}
function tt(d,a){kt();for(var c in d){if(c.charCodeAt(0)==58){var e=d[c];var b=ts(c.substring(1),e);a.j(b);}}}
function ut(f,h){kt();for(var e in f){if(e==parseInt(e)){var a=f[e];for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.s();if(zt(h,d)){return true;}}}}return false;}
function vt(a){return lt(this,a);}
function wt(c,d){kt();for(var b in c){if(b.charCodeAt(0)==58){var a=c[b];if(zt(d,a)){return true;}}}return false;}
function xt(){kt();}
function yt(){return nt(this);}
function zt(a,b){kt();if(a===b){return true;}else if(a===null){return false;}else{return a.eQ(b);}}
function Ct(a){return ot(this,a);}
function At(f,h,e){kt();var a=f[e];if(a){for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.r();if(zt(h,d)){return c.s();}}}}
function Bt(b,a){kt();return b[':'+a];}
function Dt(f,h,e){kt();var a=f[e];if(a){for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.r();if(zt(h,d)){if(a.length==1){delete f[e];}else{a.splice(g,1);}return c.s();}}}}
function Et(c,a){kt();a=':'+a;var b=c[a];delete c[a];return b;}
function ps(){}
_=ps.prototype=new kq();_.k=vt;_.o=yt;_.u=Ct;_.tI=43;_.a=null;_.b=null;_.c=0;_.d=null;var rt;function rs(b,a,c){b.a=a;b.b=c;return b;}
function ts(a,b){return rs(new qs(),a,b);}
function us(b){var a;if(lb(b,17)){a=kb(b,17);if(zt(this.a,a.r())&&zt(this.b,a.s())){return true;}}return false;}
function vs(){return this.a;}
function ws(){return this.b;}
function xs(){var a,b;a=0;b=0;if(this.a!==null){a=this.a.hC();}if(this.b!==null){b=this.b.hC();}return a^b;}
function qs(){}
_=qs.prototype=new zo();_.eQ=us;_.r=vs;_.s=ws;_.hC=xs;_.tI=44;_.a=null;_.b=null;function bt(b,a){b.a=a;return b;}
function dt(a){return As(new zs(),a.a);}
function et(c){var a,b,d;if(lb(c,17)){a=kb(c,17);b=a.r();if(lt(this.a,b)){d=ot(this.a,b);return zt(a.s(),d);}}return false;}
function ft(){return dt(this);}
function gt(){return this.a.c;}
function ys(){}
_=ys.prototype=new qr();_.l=et;_.w=ft;_.db=gt;_.tI=45;function As(c,b){var a;c.c=b;a=xr(new vr());if(c.c.b!==(kt(),rt)){yr(a,rs(new qs(),null,c.c.b));}tt(c.c.d,a);st(c.c.a,a);c.a=dq(a);return c;}
function Cs(a){return Cp(a.a);}
function Ds(a){return a.b=kb(Dp(a.a),17);}
function Es(a){if(a.b===null){throw eo(new co(),'Must call next() before remove().');}else{Ep(a.a);qt(a.c,a.b.r());a.b=null;}}
function Fs(){return Cs(this);}
function at(){return Ds(this);}
function zs(){}
_=zs.prototype=new zo();_.v=Fs;_.y=at;_.tI=0;_.a=null;_.b=null;function du(){}
_=du.prototype=new Do();_.tI=46;function un(){rn(qn(new jn()));cn(new bn());}
function gwtOnLoad(b,d,c){$moduleName=d;$moduleBase=c;if(b)try{un();}catch(a){b(d);}else{un();}}
var pb=[{},{},{1:1},{3:1},{3:1},{3:1},{3:1},{2:1},{3:1},{6:1},{6:1},{6:1},{2:1,5:1},{2:1},{7:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,10:1,11:1,12:1,13:1},{7:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{8:1},{4:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{14:1},{15:1},{16:1},{16:1},{14:1},{15:1},{17:1},{16:1},{3:1}];if (com_jldupont_project_main) {  var __gwt_initHandlers = com_jldupont_project_main.__gwt_initHandlers;  com_jldupont_project_main.onScriptLoad(gwtOnLoad);}})();