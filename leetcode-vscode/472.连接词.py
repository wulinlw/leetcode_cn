#
# @lc app=leetcode.cn id=472 lang=python3
#
# [472] 连接词
#
# https://leetcode-cn.com/problems/concatenated-words/description/
#
# algorithms
# Hard (44.70%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 5.1K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# 给定一个不含重复单词的列表，编写一个程序，返回给定单词列表中所有的连接词。
# 
# 连接词的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。
# 
# 示例:
# 
# 
# 输入:
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# 
# 输出: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# 
# 解释: "catsdogcats"由"cats", "dog" 和 "cats"组成; 
# ⁠    "dogcatsdog"由"dog", "cats"和"dog"组成; 
# ⁠    "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
# 
# 
# 说明:
# 
# 
# 给定数组的元素总数不超过 10000。
# 给定数组中元素的长度总和不超过 600000。
# 所有输入字符串只包含小写字母。
# 不需要考虑答案输出的顺序。
# 
# 
#
from typing import List
# @lc code=start
# 前缀树
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.root = TrieNode()									#构建前缀树，Leetcode 208
        for word in words:
            if word:                                            #测试用例中有空字符，需要过滤掉
                node = self.root
                for i in word: 
                    if i not in node.children:
                        node.children[i] = TrieNode()
                    node = node.children[i]
                node.isWord = True
        
        #每个字符都dfs
        # def dfs2(word, node, idx, count):                       #count是单词数
        #     if idx == len(word):                                #边界条件，跑到最后，看看是不是一个单词结尾，同时单词超过1个，只有1个的话，不算连接词
        #         return node.isWord and count>0
        #     if node.isWord:                                     #每次到一个单词结束节点，dfs，count+1
        #         if dfs2(word, self.root, idx, count+1):         #重置node到根，看看下一个字符在不在开头，cats: 位置t的时候看看s在不在根的chrildren中，不在的话，就不该在这里算一个单词
        #             return True
        #     if word[idx] not in node.children:
        #         return False
        #     else:
        #         return dfs2(word, node.children[word[idx]], idx+1, count)    #更新节点，处理下一个字符

        #只在每个单词结尾dfs
        def dfs(word, index, count):
            node = self.root
            for i in range(index, len(word)):
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                if node.isWord:
                    if i == len(word)-1:
                        return count>=1
                    if dfs(word, i+1, count+1):                 #指针指向下一个字符，单词数+1
                        return True
            return False

        re = []
        for word in words:
            # if dfs2(word, self.root, 0, 0):                    #dfs2,这个每个字符都dfs一次
            if dfs(word, 0, 0):
                re.append(word)
        return re

        

# @lc code=end
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
words = ["cat","dog","catdog"]
words = ["rfkqyuqfjkx","","vnrtysfrzrmzl","gfve","qfpd","lqdqrrcrwdnxeuo","q","klaitgdphcspij","hbsfyfv","adzpbfudkklrw","aozmixr","ife","feclhbvfuk","yeqfqojwtw","sileeztxwjl","ngbqqmbxqcqp","khhqr","dwfcayssyoqc","omwufbdfxu","zhift","kczvhsybloet","crfhpxprbsshsjxd","ilebxwbcto","yaxzfbjbkrxi","imqpzwmshlpj","ta","hbuxhwadlpto","eziwkmg","ovqzgdixrpddzp","c","wnqwqecyjyib","jy","mjfqwltvzk","tpvo","phckcyufdqml","lim","lfz","tgygdt","nhcvpf","fbrpzlk","shwywshtdgmb","bkkxcvg","monmwvytby","nuqhmfj","qtg","cwkuzyamnerp","fmwevhwlezo","ye","hbrcewjxvcezi","tiq","tfsrptug","iznorvonzjfea","gama","apwlmbzit","s","hzkosvn","nberblt","kggdgpljfisylt","mf","h","bljvkypcflsaqe","cijcyrgmqirz","iaxakholawoydvch","e","gttxwpuk","jf","xbrtspfttota","sngqvoijxuv","bztvaal","zxbshnrvbykjql","zz","mlvyoshiktodnsjj","qplci","lzqrxl","qxru","ygjtyzleizme","inx","lwhhjwsl","endjvxjyghrveu","phknqtsdtwxcktmw","wsdthzmlmbhjkm","u","pbqurqfxgqlojmws","mowsjvpvhznbsi","hdkbdxqg","ge","pzchrgef","ukmcowoe","nwhpiid","xdnnl","n","yjyssbsoc","cdzcuunkrf","uvouaghhcyvmlk","aajpfpyljt","jpyntsefxi","wjute","y","pbcnmhf","qmmidmvkn","xmywegmtuno","vuzygv","uxtrdsdfzfssmel","odjgdgzfmrazvnd","a","rdkugsbdpawxi","ivd","bbqeonycaegxfj","lrfkraoheucsvpi","eqrswgkaaaohxx","hqjtkqaqh","berbpmglbjipnuj","wogwczlkyrde","aqufowbig","snjniegvdvotu","ocedkt","bbufnxorixibbd","rzuqsyr","qghoy","evcuanuujszitaoa","wsx","glafbwzdd","znrvjqeyqi","npitruijvyllsi","objltu","ryp","nvybsfrxtlfmp","id","zoolzslgd","owijatklvjzscizr","upmsoxftumyxifyu","xucubv","fctkqlroq","zjv","wzi","ppvs","mflvioemycnphfjt","nwedtubynsb","repgcx","gsfomhvpmy","kdohe","tyycsibbeaxn","wjkfvabn","llkmagl","thkglauzgkeuly","paeurdvexqlw","akdt","ihmfrj","janxk","rqdll","cyhbsuxnlftmjc","yybwsjmajbwtuhkk","ovytgaufpjl","iwbnzhybsx","mumbh","jqmdabmyu","br","lwstjkoxbczkj","vhsgzvwiixxaob","fso","qnebmfl","ooetjiz","lq","msxphqdgz","mqhoggvrvjqrp","xbhkkfg","zxjegsyovdrmw","jav","mshoj","ax","biztkfomz","hujdmcyxdqteqja","gqgsomonv","reqqzzpw","lihdnvud","lznfhbaokxvce","fhxbldylqqewdnj","rlbskqgfvn","lfvobeyolyy","v","iwh","fpbuiujlolnjl","gvwxljbo","ypaotdzjxxrsc","mwrvel","umzpnoiei","ogwilaswn","yw","egdgye","hsrznlzrf","mwdgxaigmxpy","yaqgault","dtlg","cyvfiykmkllf","zxqyhvizqmamj","lvvgoifltzywueyp","abinmy","ppzaecvmx","qsmzc","iddymnl","uskihek","evxtehxtbthq","jvtfzddlgch","czohpyewf","ufzazyxtqxcu","brxpfymuvfvs","xrrcfuusicc","aqhlswbzievij","rv","udvmara","upityz","fecd","suxteeitxtg","dfuydrtbfypbn","cypqodxr","wikfuxwjht","jrliuaifpp","vkmxys","wvpfyfpkvgthq","rmajxis","jncxgviyu","av","nmhskodmidaj","lkfrimprrhen","uip","hstyopbvuiqc","p","vwduwmjpblqo","fnxwgqtvwztje","xwnbcuggl","iehimvoymyjasin","spsqiu","flhyfac","mqrbq","pstsxhplrrmbeddv","hnegtuxx","alsyxezjwtlwmxv","jtxytykkcku","bhhlovgcx","xhhivxnutkx","had","aysulvk","m","anhsyxli","jdkgfc","potn","lcibpxkidmwexp","gwoxjicdkv","tltienw","ngiutnuqbzi","o","tzlyb","vumnwehj","os","np","lhv","uzvgyeette","ipfvr","lpprjjalchhhcmh","k","pciulccqssaqgd","tp","dmzdzveslyjad","wtsbhgkd","eouxbldsxzm","vhtonlampljgzyve","xhnlcrldtfthul","xhflc","upgei","rlaks","yfqvnvtnqspyjbxr","phouoyhvls","voibuvbhhjcdflvl","rgorfbjrofokggaf","dqhqats","zchpicyuawpovm","yzwfor","koat","pybf","fhdzsbiyjld","gznfnqydisn","xz","po","tcjup","wygsnxk","kqlima","fgxnuohrnhg","publurhztntgmimc","zuufzphd","iucrmmmjqtcey","wnnbq","rghzyz","ukjqsjbmp","mdtrgv","vyeikgjdnml","kxwldnmi","apzuhsbssaxj","tkbkoljyodlipof","nkq","ktwtj","vgmkgjwle","t","agylw","vomtuy","jbtvitkqn","vtdxwrclpspcn","rdrls","yxfeoh","upj","myctacn","fdnor","ahqghzhoqprgkym","phiuvdv","jp","fdgpouzjwbq","hqoyefmugjvewhxu","qfzwuwe","fnsbijkeepyxry","oja","qthkcij","zpmqfbmnr","ybaibmzonzqlnmd","svo","gjftyfehik","jfrfgznuaytvaegm","aljhrx","odjq","ogwaxrssjxgvnka","zaqswwofedxj","lugpktauixp","dc","odknlbvxrs","jeobu","vqythyvzxbcgrlbg","hwc","erpbaxq","ujxcxck","rrklkb","wlrwyuy","zmg","yyhga","xwdbycdu","htedgvsrhchox","wr","suhesetv","jonqwhkwezjvjgg","sqqyrxtjkcalswq","hvyimhe","pjzdkmoue","zbphmgoxq","lbdlcumdgixjbcq","ztzdjqmadthtdmv","qcagsyqggcf","if","jpjxcjyi","chyicqibxdgkqtg","iwpdklhum","wljmg","micmun","npdbamofynykqv","ijsnfkpfy","lmq","oyjmeqvhcrvgm","mqopusqktdthpvz","fz","r","qbsqtipq","nxtsnason","xbpipyhh","topsuqomfjrd","islif","gbndakaq","bwnkxnwpzeoohlx","hrtbfnq","fguvomeepxoffg","mat","dzfpfnwbfuj","onlvy","cwcchvsasdylb","rxfcztzqopdi","ybrhodjn","oqkijy","ncvrjo","dphbfaal","xgtpdtkz","sebevsopjvciwljf","rcumyacqdapwczen","mabkapuoud","pbozezeygljfftvy","bvazmzbndl","vl","qiaixdtbhqvlzd","ffjfb","svthrfmkoxbho","cvet","ucgqyvopafyttrh","lbgihet","naiqyufxffdw","vruh","uz","ukffmudygjavem","dccamymhp","wofwgjkykm","fbuujzxhln","kmm","lzandlltowjpwsal","fapfvrmezbsjxs","wiw","sc","soqlh","hzaplclkwl","gcdqbcdwbwa","gadgt","pgowefka","juffuguqepwnfh","nbuinl","cpdxf","sox","fq","lfnrhgsxkhx","xrcorfygjxpi","mwtqjwbhgh","loc","fkglorkkvx","nlzdhucvayrz","azefobxutitrf","rlrstkcbtikklmh","ggk","sbphcejuylh","nraoenhd","zngyodiqlchxyycx","rrbhfwohfv","krzolrglgn","cpjesdzy","yoifoyg","hqqevqjugi","ahmv","xgaujnyclcjq","evhyfnlohavrj","byyvhgh","hyw","kedhvwy","ysljsqminajfipds","rglnpxfqwu","cibpynkxg","su","mbntqrlwyampdg","nig","ldhlhqdyjcfhu","jfymrbafmyoc","tyjmnhlfnrtz","dlazixtlxyvm","fbiguhsfuqo","rhymsno","rkbdlchs","ocbbwwd","astaiamnepwkya","mplirup","edkxjq","g","exlwulswtvot","tlnc","vnrrzerz","ygeraoozbtt","yyifkin","eo","ua","qgztvqdolf","rlzddjzcshvd","khxkdxflwxme","kk","zylbhoaac","cw","iizic","gcdxstpz","kjwdqeg","earjrncmmkdel","kbesuhquepj","nrzbllldgdmyrpgl","hllwnqozf","djpchowhwevbqvjj","zsmhylnjpktb","pxnktxkm","fxwiaqqb","qjwufmwresfsfaok","aa","d","iobioqm","svjgzk","khbzp","euexyudhrioi","yqsj","ngrwqpoh","rwuvd","eruffmlg","bxzovyew","faz","pmvfvyguqdi","jlxnoixsy","hyfrdngjf","ly","eibcapetpmeaid","tpnwwiif","pfgsp","kvhhwkzvtvlhhb","pjxurgqbtldims","rncplkeweoirje","akyprzzphew","wyvfpjyglzrmhfqp","ubheeqt","rmbxlcmn","taqakgim","apsbu","khwnykughmwrlk","vtdlzwpbhcsbvjno","tffmjggrmyil","schgwrrzt","mvndmua","nlwpw","glvbtkegzjs","piwllpgnlpcnezqs","xkelind","urtxsezrwz","zechoc","vfaimxrqnyiq","ybugjsblhzfravzn","btgcpqwovwp","zgxgodlhmix","sfzdknoxzassc","wgzvqkxuqrsqxs","dwneyqisozq","fg","vhfsf","uspujvqhydw","eadosqafyxbmzgr","tyff","blolplosqnfcwx","uwkl","puenodlvotb","iizudxqjvfnky","cjcywjkfvukvveq","jrxd","igwb","dftdyelydzyummmt","uvfmaicednym","oai","higfkfavgeemcgo","naefganqo","iqebfibigljbc","ulicojzjfrc","igxprunj","cymbrl","fqmwciqtynca","zjyagi","mzuejrttefhdwqc","zyiurxvf","wrjxffzbjexsh","wrxw","mhrbdxjwi","htknfa","wfrvxqdkhbwwef","vqsghhhutdget","cwupzrts","hbjnb","wpccoa","nx","howbzhaoscgyk","bilt","wqqatye","zceuuwg","jxzon","kkfj","bwsezd","ifdegsyjtswselk","xweimxlnzoh","tqthlftjblnpht","ww","ss","b","jmruuqscwjp","nxbk","wd","cqkrtbxgzg","xhppcjnq","cfq","tkkolzcfi","wblxki","ijeglxsvc","kcqjjwcwuhvzydm","gubqavlqffhrzz","hiwxrgftittd","caybc","ncsyjlzlxyyklc","poxcgnexmaajzuha","dhaccuualacyl","mtkewbprs","oncggqvr","sqqoffmwkplsgbrp","ioajuppvqluhbdet","dzwwzaelmo","afumtqugec","wglucmugwqi","zveswrjevfz","nxlbkak","pzcejvxzeoybb","fd","vewj","ivws","zjhudtpqsfc","zcmukotirrxx","zksmx","umofzhhowyftz","zbotrokaxaryxlk","ueolqk","dxmzhoq","zvu","cjl","esfmqgvxwfy","npbep","vbgjtbv","poeugoqynkbfiv","fewjjscjrei","yqssxzsydgllfzmo","urxkwcypctjkabi","wqtldwhjouas","tovdtkr","onzgeyddkqwuhnim","ffxviyvsktqrfa","qujhd","pvcz","hiyjlkxmeplnrvxg","hdykehkefp","vepcxhozpjxtreyn","liguhuxudbnh","f","ordxzm","klgohcmmbukz","yrmooliaobbnlap","dutnbetocxylcey","ywdsjegd","cr","blbxhjsgcuoxmqft","ngzdc","srfyjjumcbxole","dazwzwtdjoyuqeqj","xazjarqgfm","fxyfqbeoktcc","qrsjchxp","iltaqzawhgu","sgenjcfxr","yfikp","dvwhbyumthkiktb","walsx","jyajrkcvysicisab","brdeumb","tviihjwxdcz","dnrrgmem","ydgxlrjzucxyid","cdvdpvjlagwmg","ngnpxjkxims","gvyhnchlimsxc","w","jtizpezjl","qe","rjzv","vhnqvi","qm","iedzqswrsnfmnn","lt","utqfcqyrrwm","wtelvsqrru","fjwrhjcrtbcytn","qmqxceuohpiffaq","rmoybqjjgdyo","pmxttqftypfexlv","tg","qa","iqbqjlnpbf","kgaynkddbzllecd","tccvslp","curkxfoimnw","fvnyqkzlheruxr","iiygnzfov","coqs","oa","eiu","vzemmxtklis","lxu","nrwsjaxzwmh","tdayz","oxbbemejgosgcynf","ykbcn","hesvnctfvdsp","ku","rjhykpadahbhj","at","sxlngbtxmqr","wqrom","qzyabzrco","rbbyklndcqdj","cnsmgmwmpbgjq","krvnaf","qrwfajnfahyqocdb","fnlaozmff","vmoymbmytjvfcgt","cijyy","jdgwjbztl","swmalgbgpaplqgz","hfl","typttkrpfvx","tkzpzrscwbx","bwfqqvjcukjbsg","nxqmxr","x","eyavnz","il","dhthp","eyelg","npsoqsw","reogbmveofvusdsx","jvdrjkhxkq","qzjbrpljwuzpl","czqeevvbvcwh","vzuszqvhlmapty","yu","yldwwgezlqur","vorxwgdtgjilgydq","pknt","bgihl","ckorgrm","ixylxjmlfv","bpoaboylced","zea","igfagitkrext","ipvqq","dmoerc","oqxbypihdv","dtjrrkxro","rexuhucxpi","bvmuyarjwqpcoywa","qwdmfpwvamisns","bhopoqdsref","tmnm","cre","ktrniqwoofoeenbz","vlrfcsftapyujmw","updqikocrdyex","bcxw","eaum","oklsqebuzeziisw","fzgyhvnwjcns","dybjywyaodsyw","lmu","eocfru","ztlbggsuzctoc","ilfzpszgrgj","imqypqo","fump","sjvmsbrcfwretbie","oxpmplpcg","wmqigymr","qevdyd","gmuyytguexnyc","hwialkbjgzc","lmg","gijjy","lplrsxznfkoklxlv","xrbasbznvxas","twn","bhqultkyfq","saeq","xbuw","zd","kng","uoay","kfykd","armuwp","gtghfxf","gpucqwbihemixqmy","jedyedimaa","pbdrx","toxmxzimgfao","zlteob","adoshnx","ufgmypupei","rqyex","ljhqsaneicvaerqx","ng","sid","zagpiuiia","re","oadojxmvgqgdodw","jszyeruwnupqgmy","jxigaskpj","zpsbhgokwtfcisj","vep","ebwrcpafxzhb","gjykhz","mfomgxjphcscuxj","iwbdvusywqlsc","opvrnx","mkgiwfvqfkotpdz","inpobubzbvstk","vubuucilxyh","bci","dibmye","rlcnvnuuqfvhw","oorbyyiigppuft","swpksfdxicemjbf","goabwrqdoudf","yjutkeqakoarru","wuznnlyd","vfelxvtggkkk","mxlwbkbklbwfsvr","advraqovan","smkln","jxxvzdjlpyurxpj","ssebtpznwoytjefo","dynaiukctgrzjx","irzosjuncvh","hcnhhrajahitn","vwtifcoqepqyzwya","kddxywvgqxo","syxngevs","batvzmziq","mjewiyo","pzsupxoflq","byzhtvvpj","cqnlvlzr","akvmxzbaei","mwo","vg","ekfkuajjogbxhjii","isdbplotyak","jvkmxhtmyznha","lqjnqzrwrmgt","mbbhfli","bpeohsufree","ajrcsfogh","lucidbnlysamvy","tutjdfnvhahxy","urbrmmadea","hghv","acnjx","athltizloasimp","gu","rjfozvgmdakdhao","iephs","uztnpqhdl","rfuyp","crcszmgplszwfn","zihegt","xbspa","cjbmsamjyqqrasz","ghzlgnfoas","ljxl","cnumquohlcgt","jm","mfccj","hfedli","vtpieworwhyiucs","tdtuquartspkotm","pnkeluekvelj","ugrloq","zljmwt","fkyvqguqq","tpjidglpxqfxv","l","tvvimvroz","yy","opwyfovdz","pwlumocnyuoume","vjqpzkcfc","ihicd","dtttiixlhpikbv","goblttgvmndkqgg","gwsibcqahmyyeagk","prtvoju","lcblwidhjpu","kbu","pey","gkzrpc","bqajopjjlfthe","bc","lqs","zkndgojnjnxqsoqi","zyesldujjlp","drswybwlfyzph","xzluwbtmoxokk","bedrqfui","opajzeahv","lehdfnr","mnlpimduzgmwszc","velbhj","miwdn","wruqc","kscfodjxg","wcbm"]
o = Solution()
print(o.findAllConcatenatedWordsInADict(words))