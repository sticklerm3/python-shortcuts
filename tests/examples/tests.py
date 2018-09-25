import mock

from shortcuts import Shortcut


class BaseShortcutTest:
    def test_loads(self):
        with open(self.filepath, 'rb') as f:
            sc = Shortcut.load(f, file_format='toml')

        assert [a.itype for a in sc.actions] == self.exp_itypes

    def test_dumps_to_plist(self):
        with open(self.filepath, 'rb') as f:
            sc = Shortcut.load(f, file_format='toml')

        mocked_uuid = mock.Mock()
        mocked_uuid.uuid4.return_value = 'some-id'

        with mock.patch('shortcuts.shortcut.uuid', mocked_uuid):
            plist = sc.dumps(file_format='plist')

        assert plist == self.exp_plist


class TestSendPhotoShortcut(BaseShortcutTest):
    filepath = './examples/send_photo.toml'

    exp_itypes = [
        'is.workflow.actions.choosefrommenu',
        'is.workflow.actions.choosefrommenu',
        'is.workflow.actions.selectphoto',
        'is.workflow.actions.choosefrommenu',
        'is.workflow.actions.takephoto',
        'is.workflow.actions.choosefrommenu',
        'is.workflow.actions.setvariable',
        'is.workflow.actions.sendmessage',
    ]
    exp_plist = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.choosefrommenu</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>0</integer>\n\t\t\t\t<key>WFMenuItems</key>\n\t\t\t\t<array>\n\t\t\t\t\t<string>Select photo</string>\n\t\t\t\t\t<string>Camera</string>\n\t\t\t\t</array>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.choosefrommenu</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>1</integer>\n\t\t\t\t<key>WFMenuItemTitle</key>\n\t\t\t\t<string>Select photo</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.selectphoto</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict/>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.choosefrommenu</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>1</integer>\n\t\t\t\t<key>WFMenuItemTitle</key>\n\t\t\t\t<string>Camera</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.takephoto</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict/>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.choosefrommenu</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>2</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.setvariable</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFVariableName</key>\n\t\t\t\t<string>photo</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.sendmessage</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>IntentAppIdentifier</key>\n\t\t\t\t<string>com.apple.MobileSMS</string>\n\t\t\t\t<key>WFSendMessageActionRecipients</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t<string>Ask</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenAttachment</string>\n\t\t\t\t</dict>\n\t\t\t\t<key>WFSendMessageContent</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t<key>{7, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>photo</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>Look!\n\n￼￼</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'


class TestBase64Shortcut(BaseShortcutTest):
    filepath = './examples/base64.toml'

    exp_itypes = [
        'is.workflow.actions.gettext',
        'is.workflow.actions.setvariable',
        'is.workflow.actions.base64encode',
        'is.workflow.actions.setvariable',
        'is.workflow.actions.base64encode',
        'is.workflow.actions.setvariable',
        'is.workflow.actions.showresult',
    ]
    exp_plist = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.gettext</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFTextActionText</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>ping</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.setvariable</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFVariableName</key>\n\t\t\t\t<string>variable</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.base64encode</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFEncodeMode</key>\n\t\t\t\t<string>Encode</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.setvariable</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFVariableName</key>\n\t\t\t\t<string>variable_encoded</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.base64encode</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFEncodeMode</key>\n\t\t\t\t<string>Decode</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.setvariable</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFVariableName</key>\n\t\t\t\t<string>variable_decoded</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.showresult</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>Text</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t<key>{34, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>variable</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t<key>{54, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>variable_encoded</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t<key>{74, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>variable_decoded</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>Hello, world!\n\noriginal_variable: ￼\nvariable_encoded: ￼\nvariable_decoded: ￼\n</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'


class TestDictionaryShortcut(BaseShortcutTest):
    filepath = './examples/dictionary.toml'

    exp_itypes = [
        'is.workflow.actions.dictionary',
    ]
    exp_plist = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.dictionary</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFItems</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>WFDictionaryFieldValueItems</key>\n\t\t\t\t\t\t<array>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>some key</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>some value</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>another key</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t\t<key>{0, 1}</key>\n\t\t\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t\t\t\t\t<string>x</string>\n\t\t\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>￼</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</array>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFDictionaryFieldValue</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'


class TestGetURLShortcut(BaseShortcutTest):
    filepath = './examples/get_url.toml'

    exp_itypes = [
        'is.workflow.actions.url',
        'is.workflow.actions.downloadurl',
        'is.workflow.actions.setvariable',
        'is.workflow.actions.showresult',
    ]
    exp_plist = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.url</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFURLActionURL</key>\n\t\t\t\t<string>http://ipinfo.io/ip</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.downloadurl</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>Advanced</key>\n\t\t\t\t<true/>\n\t\t\t\t<key>ShowHeaders</key>\n\t\t\t\t<true/>\n\t\t\t\t<key>WFHTTPHeaders</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>WFDictionaryFieldValueItems</key>\n\t\t\t\t\t\t<array>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>header1</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>value1</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>authorization</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t\t<key>{0, 1}</key>\n\t\t\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t\t\t\t\t<string>authorization</string>\n\t\t\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>￼</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</array>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFDictionaryFieldValue</string>\n\t\t\t\t</dict>\n\t\t\t\t<key>WFHTTPMethod</key>\n\t\t\t\t<string>GET</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.setvariable</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFVariableName</key>\n\t\t\t\t<string>var</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.showresult</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>Text</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t<key>{10, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>var</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>response: ￼</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'


class TestIfElseShortcut(BaseShortcutTest):
    filepath = './examples/if-else.toml'

    exp_itypes = [
        'is.workflow.actions.gettext',
        'is.workflow.actions.conditional',
        'is.workflow.actions.showresult',
        'is.workflow.actions.conditional',
        'is.workflow.actions.showresult',
        'is.workflow.actions.conditional',
    ]
    exp_plist = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.gettext</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFTextActionText</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>test</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.conditional</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFCondition</key>\n\t\t\t\t<string>Equals</string>\n\t\t\t\t<key>WFConditionalActionString</key>\n\t\t\t\t<string>test</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>0</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.showresult</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>Text</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>true!</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.conditional</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>1</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.showresult</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>Text</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>false :(</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.conditional</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>2</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'


class TestMultilineShortcut(BaseShortcutTest):
    filepath = './examples/multiline.toml'

    exp_itypes = [
        'is.workflow.actions.comment',
    ]
    exp_plist = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.comment</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFCommentActionText</key>\n\t\t\t\t<string>Hi!\nThis is an example shortcut, created with python-shortcuts.\n\nSee more here: https://github.com/alexander-akhmetov/python-shortcuts\n</string>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'


class TestRepeatFlashShortcut(BaseShortcutTest):
    filepath = './examples/repeat_flash.toml'

    exp_itypes = [
        'is.workflow.actions.repeat.count',
        'is.workflow.actions.flashlight',
        'is.workflow.actions.delay',
        'is.workflow.actions.flashlight',
        'is.workflow.actions.repeat.count',
    ]
    exp_plist = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.repeat.count</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>0</integer>\n\t\t\t\t<key>WFRepeatCount</key>\n\t\t\t\t<integer>3</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.flashlight</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFFlashlightSetting</key>\n\t\t\t\t<string>On</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.delay</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFDelayTime</key>\n\t\t\t\t<real>1.0</real>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.flashlight</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFFlashlightSetting</key>\n\t\t\t\t<string>Off</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.repeat.count</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-id</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>2</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'


class TestWhatIsYourNameShortcut(BaseShortcutTest):
    filepath = './examples/what_is_your_name.toml'

    exp_itypes = [
        'is.workflow.actions.ask',
        'is.workflow.actions.setvariable',
        'is.workflow.actions.showresult',
    ]
    exp_plist = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.ask</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFAskActionPrompt</key>\n\t\t\t\t<string>What is your name?</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.setvariable</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFVariableName</key>\n\t\t\t\t<string>name</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.showresult</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>Text</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t<key>{7, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>name</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>Hello, ￼!</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'
