<template>
  <textarea
    rows="1"
    :value="value"
    @input="update($event.target.value)"
    @keypress.enter="activate"
    @keyup.enter="push">
  </textarea>
</template>


<script>
export default {
  props: ['value'],
  watch: {
    value: function(newValue) {
      /* resize textarea */
      let element = this.$el
      /* expand textbox when overflowed */
      if (element.scrollHeight > element.clientHeight) {
        element.rows += 1
      }
      /* narrow when reset */
      if (newValue === '') {
        element.rows = 1
      }
    },
  },
  data: function() {
    return {
      isReady: false,
    }
  },
  methods: {
    update: function (value) {
      this.$emit('input', value)
    },
    activate: function (e) {
      /* ignore line break */
      if (!e.shiftKey) {
        e.preventDefault()
        this.isReady = true
      }
    },
    push: function () {
      /* ignore empty value && avoid IME events */
      if (this.value === '' || !this.isReady) { return }
      /* push the text */
      this.$emit('submit')
      /* reset */
      this.isReady = false
    }
  }
};
</script>


<style lang="scss" scoped>
textarea {
  margin: 12px;
  padding: 8px;
  border-radius: 4px;
  border: 2px lightgray solid;
  resize: none;
  &:focus {
    outline: none;
    border-color: gray;
  }
}
</style>
