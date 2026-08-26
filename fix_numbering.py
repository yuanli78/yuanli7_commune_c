import re

with open('lore/gongyue.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Fix all cross-references before renumbering
content = content.replace('适用第十五条之二的惩罚程序', '适用第二十条之二的惩罚程序')
content = content.replace('不适用第十五条之一', '不适用第二十条之一')
content = content.replace('按第十条（创作者报酬）及第十条之一（奉献量记录）', '按第十五条（创作者报酬）及第十五条之一（奉献量记录）')

# Fix不可妥协条款 list key-word references
content = content.replace('第十三条（10%否决权）', '第十八条（10%否决权）')
content = content.replace('第十条之一第四款、第五款（反算法压迫）', '第十五条之一第四款、第五款（反算法压迫）')
content = content.replace('第十五条之一（劳动合同关系）', '第二十条之一（劳动合同关系）')
content = content.replace('第十五条之二（惩罚与集体利益保护）', '第二十条之二（惩罚与集体利益保护）')
content = content.replace('第十七条之二十二（反粉丝制度）', '第二十二条之二十二（反粉丝制度）')
content = content.replace('第十九条之九（正史派别立场审核标准）', '第二十四条之九（正史派别立场审核标准）')
content = content.replace('第十九条之十（自由幻想与等级幻想的区分）', '第二十四条之十（自由幻想与等级幻想的区分）')
content = content.replace('第二十条（列宁党的组织原则）', '第二十五条（列宁党的组织原则）')
content = content.replace('第二十一条（毛泽东文艺为工农兵服务原则）', '第二十六条（毛泽东文艺为工农兵服务原则）')
content = content.replace('第二十二条（反文化压迫）', '第二十七条（反文化压迫）')

# Step 2: Insert 5 new clauses after 第六原则
insert_point = '            </div>\n        </div>\n\n        <!-- 二、组织制度 -->\n        <h3>二、组织制度</h3>'
new_clauses = '''            </div>
        </div>

        <!-- 二、组织制度 -->
        <h3>二、组织制度</h3>
        <div class="section-card">
            <div class="article-item">
                <div class="article-num">第六条</div>
                <div class="article-content"><strong>（公社社员资格）</strong> 凡认同本公约第一原则所确立的共产主义路线，自愿参与集体创作或集体劳动的个人，均可申请加入公社成为社员。入社程序由委员会另行规定。社员有退社自由，退社不影响其已发布作品的集体版权归属。</div>
            </div>
            <div class="article-item">
                <div class="article-num">第七条</div>
                <div class="article-content"><strong>（公社的根本宗旨与任务）</strong> 公社以宣传共产主义为根本目的，通过集体创作、统一世界观体系和本公约的制度框架实现这一目的。公社的任务包括但不限于：组织文化生产者的集体创作，维护统一世界观的正史体系，通过收入上限和公社金制度保障创作者的基本生活，以及逐步扩大集体版权的影响力。</div>
            </div>
            <div class="article-item">
                <div class="article-num">第八条</div>
                <div class="article-content"><strong>（社员的基本义务）</strong>
                    <ul class="sub-list">
                        <li>遵守本公约及委员会制定的各项细则；</li>
                        <li>维护统一世界观的核心设定，不得在正史作品中歪曲或破坏核心设定；</li>
                        <li>参与集体创作或服务劳动，按奉献量记录制度登记劳动时间；</li>
                        <li>不得泄露平台的内部决策信息和未公开的设定资料。</li>
                    </ul>
                </div>
            </div>
            <div class="article-item">
                <div class="article-num">第九条</div>
                <div class="article-content"><strong>（社员的基本权利）</strong>
                    <ul class="sub-list">
                        <li>在公约框架内自由创作的权利；</li>
                        <li>参与全体社员大会表决和委员会选举的权利；</li>
                        <li>对其他社员及委员会的工作提出批评与自我批评的权利；</li>
                        <li>查阅公共账户账目和奉献量记录的权利。</li>
                    </ul>
                </div>
            </div>
            <div class="article-item">
                <div class="article-num">第十条</div>
                <div class="article-content"><strong>（公社与其他组织的关系原则）</strong> 公社可在不违背本公约根本原则的前提下与其他左翼组织、合作社、非营利组织进行合作。公社不接受任何形式的资本投资（包括风险投资、股权融资），不上市，不分红。不得与任何违背本公约根本立场的组织建立同盟关系。</div>
            </div>'''

content = content.replace(insert_point, new_clauses)

# Step 3: Shift ALL article-num from六条 upward by +5 using markers
map_old_to_marker = {
    '第十一条': 'XX11XX', '第十二条': 'XX12XX', '第十三条': 'XX13XX', '第十四条': 'XX14XX',
    '第十五条': 'XX15XX', '第十五条之一': 'XX15AXX', '第十五条之二': 'XX15BXX',
    '第十五条之三': 'XX15CXX', '第十五条之四': 'XX15DXX',
    '第十六条': 'XX16XX', '第十七条': 'XX17XX', '第十七条之一': 'XX17AXX',
    '第十七条之二': 'XX17BXX', '第十七条之三': 'XX17CXX', '第十七条之四': 'XX17DXX',
    '第十七条之五': 'XX17EXX', '第十七条之六': 'XX17FXX', '第十七条之七': 'XX17GXX',
    '第十七条之八': 'XX17HXX', '第十七条之九': 'XX17IXX', '第十七条之十': 'XX17JXX',
    '第十七条之十一': 'XX17KXX', '第十七条之十二': 'XX17LXX', '第十七条之十三': 'XX17MXX',
    '第十七条之十四': 'XX17NXX', '第十七条之十五': 'XX17OXX', '第十七条之十六': 'XX17PXX',
    '第十七条之十七': 'XX17QXX', '第十七条之十八': 'XX17RXX', '第十七条之十九': 'XX17SXX',
    '第十七条之二十': 'XX17TXX', '第十七条之二十一': 'XX17UXX', '第十七条之二十二': 'XX17VXX',
    '第十八条': 'XX18XX', '第十八条之一': 'XX18AXX',
    '第十九条': 'XX19XX', '第十九条之一': 'XX19AXX', '第十九条之二': 'XX19BXX',
    '第十九条之三': 'XX19CXX', '第十九条之四': 'XX19DXX', '第十九条之五': 'XX19EXX',
    '第十九条之六': 'XX19FXX', '第十九条之七': 'XX19GXX', '第十九条之八': 'XX19HXX',
    '第十九条之九': 'XX19IXX', '第十九条之十': 'XX19JXX',
    '第二十条': 'XX20XX', '第二十一条': 'XX21XX', '第二十二条': 'XX22XX',
}

for old_num, marker in map_old_to_marker.items():
    content = content.replace('class="article-num">' + old_num + '</div>', 'class="article-num">' + marker + '</div>')

map_marker_to_new = {
    'XX11XX': '第十六条', 'XX12XX': '第十七条', 'XX13XX': '第十八条', 'XX14XX': '第十九条',
    'XX15XX': '第二十条', 'XX15AXX': '第二十条之一', 'XX15BXX': '第二十条之二',
    'XX15CXX': '第二十条之三', 'XX15DXX': '第二十条之四',
    'XX16XX': '第二十一条', 'XX17XX': '第二十二条', 'XX17AXX': '第二十二条之一',
    'XX17BXX': '第二十二条之二', 'XX17CXX': '第二十二条之三', 'XX17DXX': '第二十二条之四',
    'XX17EXX': '第二十二条之五', 'XX17FXX': '第二十二条之六', 'XX17GXX': '第二十二条之七',
    'XX17HXX': '第二十二条之八', 'XX17IXX': '第二十二条之九', 'XX17JXX': '第二十二条之十',
    'XX17KXX': '第二十二条之十一', 'XX17LXX': '第二十二条之十二', 'XX17MXX': '第二十二条之十三',
    'XX17NXX': '第二十二条之十四', 'XX17OXX': '第二十二条之十五', 'XX17PXX': '第二十二条之十六',
    'XX17QXX': '第二十二条之十七', 'XX17RXX': '第二十二条之十八', 'XX17SXX': '第二十二条之十九',
    'XX17TXX': '第二十二条之二十', 'XX17UXX': '第二十二条之二十一', 'XX17VXX': '第二十二条之二十二',
    'XX18XX': '第二十三条', 'XX18AXX': '第二十三条之一',
    'XX19XX': '第二十四条', 'XX19AXX': '第二十四条之一', 'XX19BXX': '第二十四条之二',
    'XX19CXX': '第二十四条之三', 'XX19DXX': '第二十四条之四', 'XX19EXX': '第二十四条之五',
    'XX19FXX': '第二十四条之六', 'XX19GXX': '第二十四条之七', 'XX19HXX': '第二十四条之八',
    'XX19IXX': '第二十四条之九', 'XX19JXX': '第二十四条之十',
    'XX20XX': '第二十五条', 'XX21XX': '第二十六条', 'XX22XX': '第二十七条',
}

for marker, new_num in map_marker_to_new.items():
    content = content.replace(marker, new_num)

# Step 4: Fix internal text references to old article numbers
# These are references in running text (not article-num tags)
content = content.replace('第十七条（同人与正史）', '第二十二条（同人与正史）')
content = content.replace('第十七条之一（正史审定的特殊复议程序）', '第二十二条之一（正史审定的特殊复议程序）')
# Fix the references inside "第十七条之一" / "第十七条" text that refer to itself
content = content.replace('按第十七条之九及第十九条之九裁定', '按第二十二条之九及第二十四条之九裁定')
content = content.replace('适用第十九条之五（反对个人金手指）和第十九条之九', '适用第二十四条之五（反对个人金手指的压迫）和第二十四条之九')
content = content.replace('参照第十七条之十、第十七条之十一条执行', '参照第二十二条之十、第二十二条之十一条执行')
content = content.replace('适用第十七条之十二（短篇与设定投稿的审核标准）的宽松审核原则', '适用第二十二条之十二（短篇与设定投稿的审核标准）的宽松审核原则')
content = content.replace('适用第十七条之十三（番外不可再衍生番外）的原则', '适用第二十二条之十三（番外不可再衍生番外）的原则')
content = content.replace('按第十七条之一程序申诉', '按第二十二条之一程序申诉')
content = content.replace('参照第十七条之十一的标准执行', '参照第二十二条之十一的标准执行')
content = content.replace('适用第十九条之九（正史派别立场审核标准）', '适用第二十四条之九（正史派别立场审核标准）')
content = content.replace('不违反第十九条之九（派别立场审核标准）', '不违反第二十四条之九（派别立场审核标准）')
content = content.replace('是否违反第十九条之九（派别立场审核标准）', '是否违反第二十四条之九（派别立场审核标准）')
content = content.replace('不引入第十九条之五（禁止的金手指元素）', '不引入第二十四条之五（禁止的金手指元素）')
content = content.replace('是否引入第十九条之五（禁止的金手指元素）', '是否引入第二十四条之五（禁止的金手指元素）')
content = content.replace('适用第十九条之九（正史派别立场审核标准', '适用第二十四条之九（正史派别立场审核标准')
content = content.replace('第十九条之九（正史派别立场审核标准）。正史漫画不得丑化', '第二十四条之九（正史派别立场审核标准）。正史漫画不得丑化')
content = content.replace('第十九条之九（正史派别立场审核标准），不得含有', '第二十四条之九（正史派别立场审核标准），不得含有')
content = content.replace('依照第十九条之七完成解散', '依照第二十四条之七完成解散')
content = content.replace('当公司依据第十九条之七完成解散', '当公司依据第二十四条之七完成解散')

with open('lore/gongyue.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
