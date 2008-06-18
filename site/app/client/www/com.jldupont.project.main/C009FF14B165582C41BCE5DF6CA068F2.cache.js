(function(){var $wnd = window;var $doc = $wnd.document;var $moduleName, $moduleBase;var _,wt='com.google.gwt.core.client.',xt='com.google.gwt.lang.',yt='com.google.gwt.user.client.',zt='com.google.gwt.user.client.impl.',At='com.google.gwt.user.client.ui.',Bt='com.google.gwt.user.client.ui.impl.',Ct='com.jldupont.project.client.',Dt='java.lang.',Et='java.util.';function vt(){}
function jo(a){return this===a;}
function ko(){return Ao(this);}
function ho(){}
_=ho.prototype={};_.eQ=jo;_.hC=ko;_.tI=1;var o=null;function r(a){return a==null?0:a.$H?a.$H:(a.$H=t());}
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
_=v.prototype=new ho();_.eQ=C;_.hC=D;_.tI=7;function F(c,a,d,b,e){c.a=a;c.b=b;e;c.tI=d;return c;}
function bb(a,b,c){return a[b]=c;}
function cb(b,a){return b[a];}
function db(a){return a.length;}
function fb(e,d,c,b,a){return eb(e,d,c,b,0,db(b),a);}
function eb(j,i,g,c,e,a,b){var d,f,h;if((f=cb(c,e))<0){throw new bo();}h=F(new E(),f,cb(i,e),cb(g,e),j);++e;if(e<a){j=ro(j,1);for(d=0;d<f;++d){bb(h,d,eb(j,i,g,c,e,a,b));}}else{for(d=0;d<f;++d){bb(h,d,b);}}return h;}
function gb(a,b,c){if(c!==null&&a.b!=0&& !lb(c,a.b)){throw new ln();}return bb(a,b,c);}
function E(){}
_=E.prototype=new ho();_.tI=0;function jb(b,a){return !(!(b&&ob[b][a]));}
function kb(b,a){if(b!=null)jb(b.tI,a)||nb();return b;}
function lb(b,a){return b!=null&&jb(b.tI,a);}
function nb(){throw new on();}
function mb(a){if(a!==null){throw new on();}return a;}
function pb(b,d){_=d.prototype;if(b&& !(b.tI>=_.tI)){var c=b.toString;for(var a in _){b[a]=_[a];}b.toString=c;}return b;}
var ob;function Co(b,a){a;return b;}
function Bo(){}
_=Bo.prototype=new ho();_.tI=3;function tn(b,a){Co(b,a);return b;}
function sn(){}
_=sn.prototype=new Bo();_.tI=4;function mo(b,a){tn(b,a);return b;}
function lo(){}
_=lo.prototype=new sn();_.tI=5;function tb(b,a){return b;}
function sb(){}
_=sb.prototype=new lo();_.tI=8;function jc(a){a.a=xb(new wb(),a);a.b=fr(new dr());a.d=Bb(new Ab(),a);a.f=Fb(new Eb(),a);}
function kc(a){jc(a);return a;}
function mc(c){var a,b,d;a=bc(c.f);ec(c.f);b=null;if(lb(a,4)){b=tb(new sb(),kb(a,4));}else{}if(b!==null){d=o;}pc(c,false);oc(c);}
function nc(e,d){var a,b,c,f;f=false;try{pc(e,true);fc(e.f,e.b.b);re(e.a,10000);while(cc(e.f)){b=dc(e.f);c=true;try{if(b===null){return;}if(lb(b,4)){a=kb(b,4);a.p();}else{}}finally{f=gc(e.f);if(f){return;}if(c){ec(e.f);}}if(sc(zo(),d)){return;}}}finally{if(!f){oe(e.a);pc(e,false);oc(e);}}}
function oc(a){if(!mr(a.b)&& !a.e&& !a.c){qc(a,true);re(a.d,1);}}
function pc(b,a){b.c=a;}
function qc(b,a){b.e=a;}
function rc(b,a){gr(b.b,a);oc(b);}
function sc(a,b){return ao(a-b)>=100;}
function vb(){}
_=vb.prototype=new ho();_.tI=0;_.c=false;_.e=false;function pe(){pe=vt;xe=fr(new dr());{we();}}
function ne(a){pe();return a;}
function oe(a){if(a.b){se(a.c);}else{te(a.c);}or(xe,a);}
function qe(a){if(!a.b){or(xe,a);}a.bb();}
function re(b,a){if(a<=0){throw wn(new vn(),'must be positive');}oe(b);b.b=false;b.c=ue(b,a);gr(xe,b);}
function se(a){pe();$wnd.clearInterval(a);}
function te(a){pe();$wnd.clearTimeout(a);}
function ue(b,a){pe();return $wnd.setTimeout(function(){b.q();},a);}
function ve(){var a;a=o;{qe(this);}}
function we(){pe();Ce(new je());}
function ie(){}
_=ie.prototype=new ho();_.q=ve;_.tI=9;_.b=false;_.c=0;var xe;function yb(){yb=vt;pe();}
function xb(b,a){yb();b.a=a;ne(b);return b;}
function zb(){if(!this.a.c){return;}mc(this.a);}
function wb(){}
_=wb.prototype=new ie();_.bb=zb;_.tI=10;function Cb(){Cb=vt;pe();}
function Bb(b,a){Cb();b.a=a;ne(b);return b;}
function Db(){qc(this.a,false);nc(this.a,zo());}
function Ab(){}
_=Ab.prototype=new ie();_.bb=Db;_.tI=11;function Fb(b,a){b.d=a;return b;}
function bc(a){return jr(a.d.b,a.b);}
function cc(a){return a.c<a.a;}
function dc(b){var a;b.b=b.c;a=jr(b.d.b,b.c++);if(b.c>=b.a){b.c=0;}return a;}
function ec(a){nr(a.d.b,a.b);--a.a;if(a.b<=a.c){if(--a.c<0){a.c=0;}}a.b=(-1);}
function fc(b,a){b.a=a;}
function gc(a){return a.b==(-1);}
function hc(){return cc(this);}
function ic(){return dc(this);}
function Eb(){}
_=Eb.prototype=new ho();_.v=hc;_.y=ic;_.tI=0;_.a=0;_.b=(-1);_.c=0;function vc(){vc=vt;qd=fr(new dr());{kd=new kf();tf(kd);}}
function wc(b,a){vc();wf(kd,b,a);}
function xc(a,b){vc();return of(kd,a,b);}
function yc(){vc();return yf(kd,'A');}
function zc(){vc();return yf(kd,'div');}
function Ac(a){vc();return yf(kd,a);}
function Bc(){vc();return yf(kd,'img');}
function Cc(){vc();return zf(kd,'text');}
function Dc(){vc();return yf(kd,'tbody');}
function Ec(){vc();return yf(kd,'tr');}
function Fc(){vc();return yf(kd,'table');}
function cd(b,a,d){vc();var c;c=o;{bd(b,a,d);}}
function bd(b,a,c){vc();var d;if(a===pd){if(ed(b)==8192){pd=null;}}d=ad;ad=b;try{c.z(b);}finally{ad=d;}}
function dd(b,a){vc();Af(kd,b,a);}
function ed(a){vc();return Bf(kd,a);}
function fd(a){vc();pf(kd,a);}
function gd(b,a){vc();return qf(kd,b,a);}
function hd(a){vc();return Cf(kd,a);}
function id(a){vc();return rf(kd,a);}
function jd(a){vc();return sf(kd,a);}
function ld(c,a,b){vc();uf(kd,c,a,b);}
function md(a){vc();var b,c;c=true;if(qd.b>0){b=mb(jr(qd,qd.b-1));if(!(c=null.fb())){dd(a,true);fd(a);}}return c;}
function nd(b,a){vc();Df(kd,b,a);}
function od(b,a){vc();Ef(kd,b,a);}
function rd(b,a,c){vc();Ff(kd,b,a,c);}
function td(a,b,c){vc();bg(kd,a,b,c);}
function sd(a,b,c){vc();ag(kd,a,b,c);}
function ud(a,b){vc();cg(kd,a,b);}
function vd(a,b){vc();dg(kd,a,b);}
function wd(a,b){vc();eg(kd,a,b);}
function xd(b,a,c){vc();fg(kd,b,a,c);}
function yd(a,b){vc();vf(kd,a,b);}
function zd(){vc();return gg(kd);}
function Ad(){vc();return hg(kd);}
var ad=null,kd=null,pd=null,qd;function Cd(){Cd=vt;Ed=kc(new vb());}
function Dd(a){Cd();if(a===null){throw fo(new eo(),'cmd can not be null');}rc(Ed,a);}
var Ed;function be(a){if(lb(a,5)){return xc(this,kb(a,5));}return x(pb(this,Fd),a);}
function ce(){return y(pb(this,Fd));}
function Fd(){}
_=Fd.prototype=new v();_.eQ=be;_.hC=ce;_.tI=12;function ge(a){return x(pb(this,de),a);}
function he(){return y(pb(this,de));}
function de(){}
_=de.prototype=new v();_.eQ=ge;_.hC=he;_.tI=13;function le(){while((pe(),xe).b>0){oe(kb(jr((pe(),xe),0),6));}}
function me(){return null;}
function je(){}
_=je.prototype=new ho();_.C=le;_.D=me;_.tI=14;function Be(){Be=vt;De=fr(new dr());hf=fr(new dr());{df();}}
function Ce(a){Be();gr(De,a);}
function Ee(){Be();var a,b;for(a=rp(De);kp(a);){b=kb(lp(a),7);b.C();}}
function Fe(){Be();var a,b,c,d;d=null;for(a=rp(De);kp(a);){b=kb(lp(a),7);c=b.D();{d=c;}}return d;}
function af(){Be();var a,b;for(a=rp(hf);kp(a);){b=kb(lp(a),8);b.E(cf(),bf());}}
function bf(){Be();return zd();}
function cf(){Be();return Ad();}
function df(){Be();__gwt_initHandlers(function(){gf();},function(){return ff();},function(){ef();$wnd.onresize=null;$wnd.onbeforeclose=null;$wnd.onclose=null;});}
function ef(){Be();var a;a=o;{Ee();}}
function ff(){Be();var a;a=o;{return Fe();}}
function gf(){Be();var a;a=o;{af();}}
var De,hf;function wf(c,b,a){b.appendChild(a);}
function yf(b,a){return $doc.createElement(a);}
function zf(b,c){var a=$doc.createElement('INPUT');a.type=c;return a;}
function Af(c,b,a){b.cancelBubble=a;}
function Bf(b,a){switch(a.type){case 'blur':return 4096;case 'change':return 1024;case 'click':return 1;case 'dblclick':return 2;case 'focus':return 2048;case 'keydown':return 128;case 'keypress':return 256;case 'keyup':return 512;case 'load':return 32768;case 'losecapture':return 8192;case 'mousedown':return 4;case 'mousemove':return 64;case 'mouseout':return 32;case 'mouseover':return 16;case 'mouseup':return 8;case 'scroll':return 16384;case 'error':return 65536;case 'mousewheel':return 131072;case 'DOMMouseScroll':return 131072;}}
function Cf(b,a){return a.__eventBits||0;}
function Df(c,b,a){b.removeChild(a);}
function Ef(c,b,a){b.removeAttribute(a);}
function Ff(c,b,a,d){b.setAttribute(a,d);}
function bg(c,a,b,d){a[b]=d;}
function ag(c,a,b,d){a[b]=d;}
function cg(c,a,b){a.__listener=b;}
function dg(c,a,b){a.src=b;}
function eg(c,a,b){if(!b){b='';}a.innerHTML=b;}
function fg(c,b,a,d){b.style[a]=d;}
function gg(a){return $doc.body.clientHeight;}
function hg(a){return $doc.body.clientWidth;}
function jf(){}
_=jf.prototype=new ho();_.tI=0;function of(c,a,b){return a==b;}
function pf(b,a){a.preventDefault();}
function qf(f,c,d){var b=0,a=c.firstChild;while(a){var e=a.nextSibling;if(a.nodeType==1){if(d==b)return a;++b;}a=e;}return null;}
function rf(c,b){var a=b.firstChild;while(a&&a.nodeType!=1)a=a.nextSibling;return a||null;}
function sf(c,a){var b=a.parentNode;if(b==null){return null;}if(b.nodeType!=1)b=null;return b||null;}
function tf(d){$wnd.__dispatchCapturedMouseEvent=function(b){if($wnd.__dispatchCapturedEvent(b)){var a=$wnd.__captureElem;if(a&&a.__listener){cd(b,a,a.__listener);b.stopPropagation();}}};$wnd.__dispatchCapturedEvent=function(a){if(!md(a)){a.stopPropagation();a.preventDefault();return false;}return true;};$wnd.addEventListener('click',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('dblclick',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousedown',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mouseup',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousemove',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('mousewheel',$wnd.__dispatchCapturedMouseEvent,true);$wnd.addEventListener('keydown',$wnd.__dispatchCapturedEvent,true);$wnd.addEventListener('keyup',$wnd.__dispatchCapturedEvent,true);$wnd.addEventListener('keypress',$wnd.__dispatchCapturedEvent,true);$wnd.__dispatchEvent=function(b){var c,a=this;while(a&& !(c=a.__listener))a=a.parentNode;if(a&&a.nodeType!=1)a=null;if(c)cd(b,a,c);};$wnd.__captureElem=null;}
function uf(f,e,g,d){var c=0,b=e.firstChild,a=null;while(b){if(b.nodeType==1){if(c==d){a=b;break;}++c;}b=b.nextSibling;}e.insertBefore(g,a);}
function vf(c,b,a){b.__eventBits=a;b.onclick=a&1?$wnd.__dispatchEvent:null;b.ondblclick=a&2?$wnd.__dispatchEvent:null;b.onmousedown=a&4?$wnd.__dispatchEvent:null;b.onmouseup=a&8?$wnd.__dispatchEvent:null;b.onmouseover=a&16?$wnd.__dispatchEvent:null;b.onmouseout=a&32?$wnd.__dispatchEvent:null;b.onmousemove=a&64?$wnd.__dispatchEvent:null;b.onkeydown=a&128?$wnd.__dispatchEvent:null;b.onkeypress=a&256?$wnd.__dispatchEvent:null;b.onkeyup=a&512?$wnd.__dispatchEvent:null;b.onchange=a&1024?$wnd.__dispatchEvent:null;b.onfocus=a&2048?$wnd.__dispatchEvent:null;b.onblur=a&4096?$wnd.__dispatchEvent:null;b.onlosecapture=a&8192?$wnd.__dispatchEvent:null;b.onscroll=a&16384?$wnd.__dispatchEvent:null;b.onload=a&32768?$wnd.__dispatchEvent:null;b.onerror=a&65536?$wnd.__dispatchEvent:null;b.onmousewheel=a&131072?$wnd.__dispatchEvent:null;}
function mf(){}
_=mf.prototype=new jf();_.tI=0;function kf(){}
_=kf.prototype=new mf();_.tI=0;function gl(d,b,a){var c=b.parentNode;if(!c){return;}c.insertBefore(a,b);c.removeChild(b);}
function hl(b,a){if(b.h!==null){gl(b,b.h,a);}b.h=a;}
function il(b,a){xd(b.h,'height',a);}
function jl(b,c,a){nl(b,c);il(b,a);}
function kl(b,a){pl(b.h,a);}
function ll(b,a){ql(b.h,a);}
function ml(a,b){if(b===null||qo(b)==0){od(a.h,'title');}else{rd(a.h,'title',b);}}
function nl(a,b){xd(a.h,'width',b);}
function ol(b,a){yd(b.h,a|hd(b.h));}
function pl(a,b){td(a,'className',b);}
function ql(a,b){if(a===null){throw mo(new lo(),'Null widget handle. If you are creating a composite, ensure that initWidget() has been called.');}b=so(b);if(qo(b)==0){throw wn(new vn(),'Style names cannot be empty');}rl(a,b);}
function rl(b,f){var a=b.className.split(/\s+/);if(!a){return;}var g=a[0];var h=g.length;a[0]=f;for(var c=1,d=a.length;c<d;c++){var e=a[c];if(e.length>h&&(e.charAt(h)=='-'&&e.indexOf(g)==0)){a[c]=f+e.substring(h);}}b.className=a.join(' ');}
function el(){}
_=el.prototype=new ho();_.tI=0;_.h=null;function cm(a){if(a.f){throw zn(new yn(),"Should only call onAttach when the widget is detached from the browser's document");}a.f=true;ud(a.h,a);a.m();a.A();}
function dm(a){if(!a.f){throw zn(new yn(),"Should only call onDetach when the widget is attached to the browser's document");}try{a.B();}finally{a.n();ud(a.h,null);a.f=false;}}
function em(a){if(a.g!==null){a.g.ab(a);}else if(a.g!==null){throw zn(new yn(),"This widget's parent does not implement HasWidgets");}}
function fm(b,a){if(b.f){ud(b.h,null);}hl(b,a);if(b.f){ud(a,b);}}
function gm(c,b){var a;a=c.g;if(b===null){if(a!==null&&a.f){dm(c);}c.g=null;}else{if(a!==null){throw zn(new yn(),'Cannot set a new parent without first clearing the old parent');}c.g=b;if(b.f){cm(c);}}}
function hm(){}
function im(){}
function jm(a){}
function km(){}
function lm(){}
function mm(a){fm(this,a);}
function sl(){}
_=sl.prototype=new el();_.m=hm;_.n=im;_.z=jm;_.A=km;_.B=lm;_.cb=mm;_.tI=15;_.f=false;_.g=null;function Cj(b,a){gm(a,b);}
function Ej(b,a){gm(a,null);}
function Fj(){var a,b;for(b=this.w();b.v();){a=kb(b.y(),9);cm(a);}}
function ak(){var a,b;for(b=this.w();b.v();){a=kb(b.y(),9);dm(a);}}
function bk(){}
function ck(){}
function Bj(){}
_=Bj.prototype=new sl();_.m=Fj;_.n=ak;_.A=bk;_.B=ck;_.tI=16;function rg(a){a.a=zl(new tl(),a);}
function sg(a){rg(a);return a;}
function tg(c,a,b){em(a);Al(c.a,a);wc(b,a.h);Cj(c,a);}
function vg(b,c){var a;if(c.g!==b){return false;}Ej(b,c);a=c.h;nd(jd(a),a);am(b.a,c);return true;}
function wg(){return El(this.a);}
function xg(a){return vg(this,a);}
function qg(){}
_=qg.prototype=new Bj();_.w=wg;_.ab=xg;_.tI=17;function jg(a){sg(a);a.cb(zc());xd(a.h,'position','relative');xd(a.h,'overflow','hidden');return a;}
function kg(a,b){tg(a,b,a.h);}
function lg(b,d,a,c){em(d);ng(b,d,a,c);kg(b,d);}
function ng(c,e,b,d){var a;a=e.h;if(b==(-1)&&d==(-1)){og(a);}else{xd(a,'position','absolute');xd(a,'left',b+'px');xd(a,'top',d+'px');}}
function og(a){xd(a,'left','');xd(a,'top','');xd(a,'position','');}
function pg(b){var a;a=vg(this,b);if(a){og(b.h);}return a;}
function ig(){}
_=ig.prototype=new qg();_.ab=pg;_.tI=18;function qi(a){a.e=gi(new bi());}
function ri(a){qi(a);a.d=Fc();a.a=Dc();wc(a.d,a.a);a.cb(a.d);ol(a,1);return a;}
function si(c,a){var b;b=ah(c);if(a>=b||a<0){throw Cn(new Bn(),'Row index: '+a+', Row size: '+b);}}
function ti(e,c,b,a){var d;d=Ah(e.b,c,b);zi(e,d,a);return d;}
function vi(c,b,a){return b.rows[a].cells.length;}
function wi(a){return xi(a,a.a);}
function xi(b,a){return a.rows.length;}
function yi(b,a){var c;if(a!=ah(b)){si(b,a);}c=Ec();ld(b.a,c,a);return a;}
function zi(d,c,a){var b,e;b=id(c);e=null;if(b!==null){e=ii(d.e,b);}if(e!==null){Ai(d,e);return true;}else{if(a){wd(c,'');}return false;}}
function Ai(b,c){var a;if(c.g!==b){return false;}Ej(b,c);a=c.h;nd(jd(a),a);li(b.e,a);return true;}
function Bi(a,b){td(a.d,'border',''+b);}
function Ci(b,a){b.b=a;}
function Di(b,a){sd(b.d,'cellPadding',a);}
function Ei(b,a){sd(b.d,'cellSpacing',a);}
function Fi(b,a){b.c=a;ai(b.c);}
function aj(d,b,a,e){var c;ch(d,b,a);if(e!==null){em(e);c=ti(d,b,a,true);ji(d.e,e);wc(c,e.h);Cj(d,e);}}
function bj(){return mi(this.e);}
function cj(a){switch(ed(a)){case 1:{break;}default:}}
function dj(a){return Ai(this,a);}
function mh(){}
_=mh.prototype=new Bj();_.w=bj;_.z=cj;_.ab=dj;_.tI=19;_.a=null;_.b=null;_.c=null;_.d=null;function Dg(a){ri(a);Ci(a,Ag(new zg(),a));Fi(a,Eh(new Dh(),a));return a;}
function Fg(b,a){si(b,a);return vi(b,b.a,a);}
function ah(a){return wi(a);}
function bh(b,a){return yi(b,a);}
function ch(e,d,b){var a,c;dh(e,d);if(b<0){throw Cn(new Bn(),'Cannot create a column with a negative index: '+b);}a=Fg(e,d);c=b+1-a;if(c>0){eh(e.a,d,c);}}
function dh(d,b){var a,c;if(b<0){throw Cn(new Bn(),'Cannot create a row with a negative index: '+b);}c=ah(d);for(a=c;a<=b;a++){bh(d,a);}}
function eh(f,d,c){var e=f.rows[d];for(var b=0;b<c;b++){var a=$doc.createElement('td');e.appendChild(a);}}
function yg(){}
_=yg.prototype=new mh();_.tI=20;function wh(b,a){b.a=a;return b;}
function yh(c,b,a){ch(c.a,b,a);return zh(c,c.a.a,b,a);}
function zh(e,d,c,a){var b=d.rows[c].cells[a];return b==null?null:b;}
function Ah(c,b,a){return zh(c,c.a.a,b,a);}
function Bh(e,d,b,a){var c;ch(e.a,d,b);c=zh(e,e.a.a,d,b);td(c,'align',a.a);}
function Ch(c,b,a,d){ch(c.a,b,a);td(zh(c,c.a.a,b,a),'width',d);}
function vh(){}
_=vh.prototype=new ho();_.tI=0;function Ag(b,a){wh(b,a);return b;}
function Cg(d,c,b,a){sd(yh(d,c,b),'colSpan',a);}
function zg(){}
_=zg.prototype=new vh();_.tI=0;function hh(){hh=vt;wm(),ym;}
function gh(b,a){wm(),ym;jh(b,a);return b;}
function ih(b,a){switch(ed(a)){case 1:break;case 4096:case 2048:break;case 128:case 512:case 256:break;}}
function jh(b,a){fm(b,a);ol(b,7041);}
function kh(a){ih(this,a);}
function lh(a){jh(this,a);}
function fh(){}
_=fh.prototype=new sl();_.z=kh;_.cb=lh;_.tI=21;function oh(a){{rh(a);}}
function ph(b,a){b.b=a;oh(b);return b;}
function rh(a){while(++a.a<a.b.b.b){if(jr(a.b.b,a.a)!==null){return;}}}
function sh(a){return a.a<a.b.b.b;}
function th(){return sh(this);}
function uh(){var a;if(!sh(this)){throw new rt();}a=jr(this.b.b,this.a);rh(this);return a;}
function nh(){}
_=nh.prototype=new ho();_.v=th;_.y=uh;_.tI=0;_.a=(-1);function Eh(b,a){b.b=a;return b;}
function ai(a){if(a.a===null){a.a=Ac('colgroup');ld(a.b.d,a.a,0);wc(a.a,Ac('col'));}}
function Dh(){}
_=Dh.prototype=new ho();_.tI=0;_.a=null;function fi(a){a.b=fr(new dr());}
function gi(a){fi(a);return a;}
function ii(c,a){var b;b=oi(a);if(b<0){return null;}return kb(jr(c.b,b),9);}
function ji(b,c){var a;if(b.a===null){a=b.b.b;gr(b.b,c);}else{a=b.a.a;pr(b.b,a,c);b.a=b.a.b;}pi(c.h,a);}
function ki(c,a,b){ni(a);pr(c.b,b,null);c.a=di(new ci(),b,c.a);}
function li(c,a){var b;b=oi(a);ki(c,a,b);}
function mi(a){return ph(new nh(),a);}
function ni(a){a['__widgetID']=null;}
function oi(a){var b=a['__widgetID'];return b==null?-1:b;}
function pi(a,b){a['__widgetID']=b;}
function bi(){}
_=bi.prototype=new ho();_.tI=0;_.a=null;function di(c,a,b){c.a=a;c.b=b;return c;}
function ci(){}
_=ci.prototype=new ho();_.tI=0;_.a=0;_.b=null;function jj(){jj=vt;kj=hj(new gj(),'center');hj(new gj(),'left');hj(new gj(),'right');}
var kj;function hj(b,a){b.a=a;return b;}
function gj(){}
_=gj.prototype=new ho();_.tI=0;_.a=null;function xj(){xj=vt;ws(new Dr());}
function vj(a){xj();wj(a,sj(new rj(),a));kl(a,'gwt-Image');return a;}
function wj(b,a){b.a=a;}
function yj(a,b){uj(a.a,a,b);}
function zj(a){switch(ed(a)){case 1:{break;}case 4:case 8:case 64:case 16:case 32:{break;}case 131072:break;case 32768:{break;}case 65536:{break;}}}
function oj(){}
_=oj.prototype=new sl();_.z=zj;_.tI=22;_.a=null;function pj(){}
_=pj.prototype=new ho();_.tI=0;function sj(b,a){a.cb(Bc());ol(a,229501);return b;}
function uj(b,a,c){vd(a.h,c);}
function rj(){}
_=rj.prototype=new pj();_.tI=0;function jk(){jk=vt;ok=ws(new Dr());}
function ik(b,a){jk();jg(b);if(a===null){a=kk();}b.cb(a);cm(b);return b;}
function lk(){jk();return mk(null);}
function mk(c){jk();var a,b;b=kb(Cs(ok,c),10);if(b!==null){return b;}a=null;if(ok.c==0){nk();}Ds(ok,c,b=ik(new dk(),a));return b;}
function kk(){jk();return $doc.body;}
function nk(){jk();Ce(new ek());}
function dk(){}
_=dk.prototype=new ig();_.tI=23;var ok;function gk(){var a,b;for(b=kq(yq((jk(),ok)));rq(b);){a=kb(sq(b),10);if(a.f){dm(a);}}}
function hk(){return null;}
function ek(){}
_=ek.prototype=new ho();_.C=gk;_.D=hk;_.tI=24;function Dk(){Dk=vt;wm(),ym;al=Ak(new zk(),'center');Ak(new zk(),'justify');Ak(new zk(),'left');Ak(new zk(),'right');}
function Ck(b,a){Dk();gh(b,a);ol(b,1024);return b;}
function Fk(b,a){td(b.h,'value',a!==null?a:'');}
function Ek(b,a){xd(b.h,'textAlign',a.a);}
function bl(a){var b;ih(this,a);b=ed(a);}
function yk(){}
_=yk.prototype=new fh();_.z=bl;_.tI=25;var al;function dl(){dl=vt;Dk();}
function cl(a){dl();Ck(a,Cc());kl(a,'gwt-TextBox');return a;}
function xk(){}
_=xk.prototype=new yk();_.tI=26;function Ak(b,a){b.a=a;return b;}
function zk(){}
_=zk.prototype=new ho();_.tI=0;_.a=null;function zl(b,a){b.a=fb('[Lcom.google.gwt.user.client.ui.Widget;',[0],[9],[4],null);return b;}
function Al(a,b){Dl(a,b,a.b);}
function Cl(b,c){var a;for(a=0;a<b.b;++a){if(b.a[a]===c){return a;}}return (-1);}
function Dl(d,e,a){var b,c;if(a<0||a>d.b){throw new Bn();}if(d.b==d.a.a){c=fb('[Lcom.google.gwt.user.client.ui.Widget;',[0],[9],[d.a.a*2],null);for(b=0;b<d.a.a;++b){gb(c,b,d.a[b]);}d.a=c;}++d.b;for(b=d.b-1;b>a;--b){gb(d.a,b,d.a[b-1]);}gb(d.a,a,e);}
function El(a){return vl(new ul(),a);}
function Fl(c,b){var a;if(b<0||b>=c.b){throw new Bn();}--c.b;for(a=b;a<c.b;++a){gb(c.a,a,c.a[a+1]);}gb(c.a,c.b,null);}
function am(b,c){var a;a=Cl(b,c);if(a==(-1)){throw new rt();}Fl(b,a);}
function tl(){}
_=tl.prototype=new ho();_.tI=0;_.a=null;_.b=0;function vl(b,a){b.b=a;return b;}
function xl(){return this.a<this.b.b-1;}
function yl(){if(this.a>=this.b.b){throw new rt();}return this.b.a[++this.a];}
function ul(){}
_=ul.prototype=new ho();_.v=xl;_.y=yl;_.tI=0;_.a=(-1);function wm(){wm=vt;xm=qm(new om());ym=xm!==null?vm(new nm()):xm;}
function vm(a){wm();return a;}
function nm(){}
_=nm.prototype=new ho();_.tI=0;var xm,ym;function rm(){rm=vt;wm();}
function pm(a){sm(a);tm(a);um(a);}
function qm(a){rm();vm(a);pm(a);return a;}
function sm(b){return function(a){if(this.parentNode.onblur){this.parentNode.onblur(a);}};}
function tm(b){return function(a){if(this.parentNode.onfocus){this.parentNode.onfocus(a);}};}
function um(a){return function(){this.firstChild.focus();};}
function om(){}
_=om.prototype=new nm();_.tI=0;function Am(a){a.cb(yc());return a;}
function Cm(b,a){rd(b.h,'href',a===null?'':a);}
function Dm(b,a){rd(b.h,'id',a===null?'':a);}
function Em(c,d){var a,b;a=c.h;b=gd(a,0);if(b===null){b=Bc();ld(a,b,0);}vd(b,d);}
function Fm(b,a){rd(b.h,'target',a===null?'':a);}
function zm(){}
_=zm.prototype=new sl();_.tI=27;function en(a){a.f=Dg(new yg());a.b=Am(new zm());a.a=Am(new zm());a.d=Am(new zm());a.c=Am(new zm());a.e=cl(new xk());}
function gn(a){en(a);return a;}
function hn(e){var a,b,c,d;lk();d=lk();jl(d,'100%','100%');ll(d,'rootPanel');kl(d,'rootPanel');lg(d,e.f,60,0);Bi(e.f,2);jl(e.f,'377px','270px');Ei(e.f,5);Di(e.f,5);aj(e.f,1,0,e.b);Bh(e.f.b,1,0,(jj(),kj));Fm(e.b,'_blank');Cm(e.b,'http://www.linkedin.com/in/JeanLouDupont');Dm(e.b,'link_linkedin');Em(e.b,'linkedin.gif');aj(e.f,1,1,e.a);Bh(e.f.b,1,1,(jj(),kj));Fm(e.a,'_blank');Cm(e.a,'http://jldupont.blogspot.com');Dm(e.a,'link_blog');Em(e.a,'blog.jpg');aj(e.f,2,0,e.d);Bh(e.f.b,2,0,(jj(),kj));Fm(e.d,'_blank');Cm(e.d,'http://wiki.jldupont.com');Dm(e.d,'link_wiki');Em(e.d,'wiki.png');aj(e.f,2,1,e.c);Bh(e.f.b,2,1,(jj(),kj));Fm(e.c,'_blank');Cm(e.c,'http://code.google.com/u/JeanLou.Dupont/');Dm(e.c,'link_projects');Em(e.c,'projects.jpg');aj(e.f,0,0,e.e);kl(e.e,'title');Ek(e.e,(Dk(),al));ml(e.e,'title');Bh(e.f.b,0,0,(jj(),kj));Fk(e.e,"Jean-Lou Dupont's WEB site");Cg(e.f.b,0,0,2);nl(e.e,'100%');c=Dg(new yg());lg(d,c,330,367);jl(c,'107px','40px');b=vj(new oj());aj(c,0,0,b);Ch(c.b,0,0,'43px');yj(b,'gwt.png');a=vj(new oj());aj(c,0,1,a);Ch(c.b,0,1,'50px');yj(a,'gae.png');Dd(new bn());cf(),bf();}
function jn(b,a){}
function an(){}
_=an.prototype=new ho();_.E=jn;_.tI=28;function dn(){cf(),bf();}
function bn(){}
_=bn.prototype=new ho();_.p=dn;_.tI=29;function ln(){}
_=ln.prototype=new lo();_.tI=30;function on(){}
_=on.prototype=new lo();_.tI=31;function wn(b,a){mo(b,a);return b;}
function vn(){}
_=vn.prototype=new lo();_.tI=32;function zn(b,a){mo(b,a);return b;}
function yn(){}
_=yn.prototype=new lo();_.tI=33;function Cn(b,a){mo(b,a);return b;}
function Bn(){}
_=Bn.prototype=new lo();_.tI=34;function ao(a){return a<0?-a:a;}
function bo(){}
_=bo.prototype=new lo();_.tI=35;function fo(b,a){mo(b,a);return b;}
function eo(){}
_=eo.prototype=new lo();_.tI=36;function qo(a){return a.length;}
function ro(b,a){return b.substr(a,b.length-a);}
function so(c){var a=c.replace(/^(\s*)/,'');var b=a.replace(/\s*$/,'');return b;}
function to(a,b){return String(a)==b;}
function uo(a){if(!lb(a,1))return false;return to(this,a);}
function wo(){var a=vo;if(!a){a=vo={};}var e=':'+this;var b=a[e];if(b==null){b=0;var f=this.length;var d=f<64?1:f/32|0;for(var c=0;c<f;c+=d){b<<=1;b+=this.charCodeAt(c);}b|=0;a[e]=b;}return b;}
_=String.prototype;_.eQ=uo;_.hC=wo;_.tI=2;var vo=null;function zo(){return new Date().getTime();}
function Ao(a){return s(a);}
function Fo(b,a){mo(b,a);return b;}
function Eo(){}
_=Eo.prototype=new lo();_.tI=37;function cp(d,a,b){var c;while(a.v()){c=a.y();if(b===null?c===null:b.eQ(c)){return a;}}return null;}
function ep(a){throw Fo(new Eo(),'add');}
function fp(b){var a;a=cp(this,this.w(),b);return a!==null;}
function bp(){}
_=bp.prototype=new ho();_.j=ep;_.l=fp;_.tI=0;function qp(b,a){throw Cn(new Bn(),'Index: '+a+', Size: '+b.b);}
function rp(a){return ip(new hp(),a);}
function sp(b,a){throw Fo(new Eo(),'add');}
function tp(a){this.i(this.db(),a);return true;}
function up(e){var a,b,c,d,f;if(e===this){return true;}if(!lb(e,14)){return false;}f=kb(e,14);if(this.db()!=f.db()){return false;}c=rp(this);d=f.w();while(kp(c)){a=lp(c);b=lp(d);if(!(a===null?b===null:a.eQ(b))){return false;}}return true;}
function vp(){var a,b,c,d;c=1;a=31;b=rp(this);while(kp(b)){d=lp(b);c=31*c+(d===null?0:d.hC());}return c;}
function wp(){return rp(this);}
function xp(a){throw Fo(new Eo(),'remove');}
function gp(){}
_=gp.prototype=new bp();_.i=sp;_.j=tp;_.eQ=up;_.hC=vp;_.w=wp;_.F=xp;_.tI=38;function ip(b,a){b.c=a;return b;}
function kp(a){return a.a<a.c.db();}
function lp(a){if(!kp(a)){throw new rt();}return a.c.t(a.b=a.a++);}
function mp(a){if(a.b<0){throw new yn();}a.c.F(a.b);a.a=a.b;a.b=(-1);}
function np(){return kp(this);}
function op(){return lp(this);}
function hp(){}
_=hp.prototype=new ho();_.v=np;_.y=op;_.tI=0;_.a=0;_.b=(-1);function wq(f,d,e){var a,b,c;for(b=rs(f.o());ks(b);){a=ls(b);c=a.r();if(d===null?c===null:d.eQ(c)){if(e){ms(b);}return a;}}return null;}
function xq(b){var a;a=b.o();return Ap(new zp(),b,a);}
function yq(b){var a;a=Bs(b);return iq(new hq(),b,a);}
function zq(a){return wq(this,a,false)!==null;}
function Aq(d){var a,b,c,e,f,g,h;if(d===this){return true;}if(!lb(d,15)){return false;}f=kb(d,15);c=xq(this);e=f.x();if(!ar(c,e)){return false;}for(a=Cp(c);dq(a);){b=eq(a);h=this.u(b);g=f.u(b);if(h===null?g!==null:!h.eQ(g)){return false;}}return true;}
function Bq(b){var a;a=wq(this,b,false);return a===null?null:a.s();}
function Cq(){var a,b,c;b=0;for(c=rs(this.o());ks(c);){a=ls(c);b+=a.hC();}return b;}
function Dq(){return xq(this);}
function yp(){}
_=yp.prototype=new ho();_.k=zq;_.eQ=Aq;_.u=Bq;_.hC=Cq;_.x=Dq;_.tI=39;function ar(e,b){var a,c,d;if(b===e){return true;}if(!lb(b,16)){return false;}c=kb(b,16);if(c.db()!=e.db()){return false;}for(a=c.w();a.v();){d=a.y();if(!e.l(d)){return false;}}return true;}
function br(a){return ar(this,a);}
function cr(){var a,b,c;a=0;for(b=this.w();b.v();){c=b.y();if(c!==null){a+=c.hC();}}return a;}
function Eq(){}
_=Eq.prototype=new bp();_.eQ=br;_.hC=cr;_.tI=40;function Ap(b,a,c){b.a=a;b.b=c;return b;}
function Cp(b){var a;a=rs(b.b);return bq(new aq(),b,a);}
function Dp(a){return this.a.k(a);}
function Ep(){return Cp(this);}
function Fp(){return this.b.a.c;}
function zp(){}
_=zp.prototype=new Eq();_.l=Dp;_.w=Ep;_.db=Fp;_.tI=41;function bq(b,a,c){b.a=c;return b;}
function dq(a){return a.a.v();}
function eq(b){var a;a=b.a.y();return a.r();}
function fq(){return dq(this);}
function gq(){return eq(this);}
function aq(){}
_=aq.prototype=new ho();_.v=fq;_.y=gq;_.tI=0;function iq(b,a,c){b.a=a;b.b=c;return b;}
function kq(b){var a;a=rs(b.b);return pq(new oq(),b,a);}
function lq(a){return As(this.a,a);}
function mq(){return kq(this);}
function nq(){return this.b.a.c;}
function hq(){}
_=hq.prototype=new bp();_.l=lq;_.w=mq;_.db=nq;_.tI=0;function pq(b,a,c){b.a=c;return b;}
function rq(a){return a.a.v();}
function sq(a){var b;b=a.a.y().s();return b;}
function tq(){return rq(this);}
function uq(){return sq(this);}
function oq(){}
_=oq.prototype=new ho();_.v=tq;_.y=uq;_.tI=0;function er(a){{hr(a);}}
function fr(a){er(a);return a;}
function gr(b,a){zr(b.a,b.b++,a);return true;}
function hr(a){a.a=z();a.b=0;}
function jr(b,a){if(a<0||a>=b.b){qp(b,a);}return vr(b.a,a);}
function kr(b,a){return lr(b,a,0);}
function lr(c,b,a){if(a<0){qp(c,a);}for(;a<c.b;++a){if(ur(b,vr(c.a,a))){return a;}}return (-1);}
function mr(a){return a.b==0;}
function nr(c,a){var b;b=jr(c,a);xr(c.a,a,1);--c.b;return b;}
function or(c,b){var a;a=kr(c,b);if(a==(-1)){return false;}nr(c,a);return true;}
function pr(d,a,b){var c;c=jr(d,a);zr(d.a,a,b);return c;}
function rr(a,b){if(a<0||a>this.b){qp(this,a);}qr(this.a,a,b);++this.b;}
function sr(a){return gr(this,a);}
function qr(a,b,c){a.splice(b,0,c);}
function tr(a){return kr(this,a)!=(-1);}
function ur(a,b){return a===b||a!==null&&a.eQ(b);}
function wr(a){return jr(this,a);}
function vr(a,b){return a[b];}
function yr(a){return nr(this,a);}
function xr(a,c,b){a.splice(c,b);}
function zr(a,b,c){a[b]=c;}
function Ar(){return this.b;}
function dr(){}
_=dr.prototype=new gp();_.i=rr;_.j=sr;_.l=tr;_.t=wr;_.F=yr;_.db=Ar;_.tI=42;_.a=null;_.b=0;function ys(){ys=vt;Fs=ft();}
function vs(a){{xs(a);}}
function ws(a){ys();vs(a);return a;}
function xs(a){a.a=z();a.d=A();a.b=pb(Fs,v);a.c=0;}
function zs(b,a){if(lb(a,1)){return jt(b.d,kb(a,1))!==Fs;}else if(a===null){return b.b!==Fs;}else{return it(b.a,a,a.hC())!==Fs;}}
function As(a,b){if(a.b!==Fs&&ht(a.b,b)){return true;}else if(et(a.d,b)){return true;}else if(ct(a.a,b)){return true;}return false;}
function Bs(a){return ps(new gs(),a);}
function Cs(c,a){var b;if(lb(a,1)){b=jt(c.d,kb(a,1));}else if(a===null){b=c.b;}else{b=it(c.a,a,a.hC());}return b===Fs?null:b;}
function Ds(c,a,d){var b;{b=c.b;c.b=d;}if(b===Fs){++c.c;return null;}else{return b;}}
function Es(c,a){var b;if(lb(a,1)){b=mt(c.d,kb(a,1));}else if(a===null){b=c.b;c.b=pb(Fs,v);}else{b=lt(c.a,a,a.hC());}if(b===Fs){return null;}else{--c.c;return b;}}
function at(e,c){ys();for(var d in e){if(d==parseInt(d)){var a=e[d];for(var f=0,b=a.length;f<b;++f){c.j(a[f]);}}}}
function bt(d,a){ys();for(var c in d){if(c.charCodeAt(0)==58){var e=d[c];var b=bs(c.substring(1),e);a.j(b);}}}
function ct(f,h){ys();for(var e in f){if(e==parseInt(e)){var a=f[e];for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.s();if(ht(h,d)){return true;}}}}return false;}
function dt(a){return zs(this,a);}
function et(c,d){ys();for(var b in c){if(b.charCodeAt(0)==58){var a=c[b];if(ht(d,a)){return true;}}}return false;}
function ft(){ys();}
function gt(){return Bs(this);}
function ht(a,b){ys();if(a===b){return true;}else if(a===null){return false;}else{return a.eQ(b);}}
function kt(a){return Cs(this,a);}
function it(f,h,e){ys();var a=f[e];if(a){for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.r();if(ht(h,d)){return c.s();}}}}
function jt(b,a){ys();return b[':'+a];}
function lt(f,h,e){ys();var a=f[e];if(a){for(var g=0,b=a.length;g<b;++g){var c=a[g];var d=c.r();if(ht(h,d)){if(a.length==1){delete f[e];}else{a.splice(g,1);}return c.s();}}}}
function mt(c,a){ys();a=':'+a;var b=c[a];delete c[a];return b;}
function Dr(){}
_=Dr.prototype=new yp();_.k=dt;_.o=gt;_.u=kt;_.tI=43;_.a=null;_.b=null;_.c=0;_.d=null;var Fs;function Fr(b,a,c){b.a=a;b.b=c;return b;}
function bs(a,b){return Fr(new Er(),a,b);}
function cs(b){var a;if(lb(b,17)){a=kb(b,17);if(ht(this.a,a.r())&&ht(this.b,a.s())){return true;}}return false;}
function ds(){return this.a;}
function es(){return this.b;}
function fs(){var a,b;a=0;b=0;if(this.a!==null){a=this.a.hC();}if(this.b!==null){b=this.b.hC();}return a^b;}
function Er(){}
_=Er.prototype=new ho();_.eQ=cs;_.r=ds;_.s=es;_.hC=fs;_.tI=44;_.a=null;_.b=null;function ps(b,a){b.a=a;return b;}
function rs(a){return is(new hs(),a.a);}
function ss(c){var a,b,d;if(lb(c,17)){a=kb(c,17);b=a.r();if(zs(this.a,b)){d=Cs(this.a,b);return ht(a.s(),d);}}return false;}
function ts(){return rs(this);}
function us(){return this.a.c;}
function gs(){}
_=gs.prototype=new Eq();_.l=ss;_.w=ts;_.db=us;_.tI=45;function is(c,b){var a;c.c=b;a=fr(new dr());if(c.c.b!==(ys(),Fs)){gr(a,Fr(new Er(),null,c.c.b));}bt(c.c.d,a);at(c.c.a,a);c.a=rp(a);return c;}
function ks(a){return kp(a.a);}
function ls(a){return a.b=kb(lp(a.a),17);}
function ms(a){if(a.b===null){throw zn(new yn(),'Must call next() before remove().');}else{mp(a.a);Es(a.c,a.b.r());a.b=null;}}
function ns(){return ks(this);}
function os(){return ls(this);}
function hs(){}
_=hs.prototype=new ho();_.v=ns;_.y=os;_.tI=0;_.a=null;_.b=null;function rt(){}
_=rt.prototype=new lo();_.tI=46;function kn(){hn(gn(new an()));Am(new zm());}
function gwtOnLoad(b,d,c){$moduleName=d;$moduleBase=c;if(b)try{kn();}catch(a){b(d);}else{kn();}}
var ob=[{},{},{1:1},{3:1},{3:1},{3:1},{3:1},{2:1},{3:1},{6:1},{6:1},{6:1},{2:1,5:1},{2:1},{7:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,10:1,11:1,12:1,13:1},{7:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{9:1,11:1,12:1,13:1},{8:1},{4:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{3:1},{14:1},{15:1},{16:1},{16:1},{14:1},{15:1},{17:1},{16:1},{3:1}];if (com_jldupont_project_main) {  var __gwt_initHandlers = com_jldupont_project_main.__gwt_initHandlers;  com_jldupont_project_main.onScriptLoad(gwtOnLoad);}})();