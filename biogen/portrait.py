from docxtpl import InlineImage


class VersentInlinePortrait(InlineImage):
    def _insert_image(self):
        pic = self.tpl.docx._part.new_pic_inline(
            self.image_descriptor,
            self.width,
            self.height
        ).xml

        # switch the default rectangle style to the green circle
        pic = pic.replace('<a:prstGeom prst="rect"/>', green_circle_xml)

        return '</w:t></w:r><w:r><w:drawing>%s</w:drawing></w:r><w:r>' \
               '<w:t xml:space="preserve">' % pic


# This somehow draws a circle around the portrait
green_circle_xml = """\
<a:prstGeom prst="ellipse">
    <a:avLst/>
</a:prstGeom>
<a:ln w="63500" cap="rnd">
    <a:solidFill>
        <a:srgbClr val="92D050"/>
    </a:solidFill>
</a:ln>
<a:effectLst/>
<a:scene3d>
    <a:camera prst="orthographicFront"/>
    <a:lightRig rig="contrasting" dir="t">
        <a:rot lat="0" lon="0" rev="3000000"/>
    </a:lightRig>
</a:scene3d>
<a:sp3d contourW="7620">
    <a:bevelT w="95250" h="31750"/>
    <a:contourClr>
        <a:srgbClr val="333333"/>
    </a:contourClr>
</a:sp3d>\
"""